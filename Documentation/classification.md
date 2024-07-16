# Step 1: Extract text from img invoices and load JSON metadata

```bash
import pandas as pd
import json
import os
from PIL import Image
import pytesseract


def load_json_data(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)
    return data

def extract_text_from_img(img_path):
    # Open the image file
    img = Image.open(img_path)

    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(img)

    return text

# Directory containing the Image invoices and JSON metadata
img_dir = '/path/to/image/folder'
json_dir = '/path/to/json/folder'

# Extracted data
data = []

# Process each Image and corresponding JSON file
for img_filename in os.listdir(img_dir):
    if img_filename.endswith('.jpg'):
        img_path = os.path.join(img_dir, img_filename)
        json_filename = img_filename.replace('.jpg', '.json')
        json_path = os.path.join(json_dir, json_filename)
        
        # Extract text from Image
        img_text = extract_text_from_img(img_path)

        
        # Load JSON data
        json_data = load_json_data(json_path)
        
        # Combine the data
        combined_data = {
            'text': img_text,
            'company': json_data.get('company', ''),
            'date': json_data.get('date', ''),
            'address': json_data.get('address', ''),
            'total': json_data.get('total', '0.00')
        }
        
        data.append(combined_data)

# Convert to DataFrame
df = pd.DataFrame(data)

```
 
# Step 2: Preprocess the data

```bash
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Function to clean 'total' field by removing currency symbols and converting to float
def clean_total(total):
    if isinstance(total, str):
        total = total.replace('RM', '').replace('$', '').replace(',', '').strip()
        if total == '':
            return np.nan  # or any other appropriate handling for missing values
    return float(total)


# Clean 'total' field
df['total'] = df['total'].apply(clean_total)

# Encode categorical variables (if any)
label_encoder = LabelEncoder()
df['address'] = label_encoder.fit_transform(df['address'])

# Vectorize the text data

vectorizer = TfidfVectorizer(max_features=1000, min_df=2, max_df=0.95)
text_features = vectorizer.fit_transform(df['text']).toarray()
print(text_features)


# Select features and label
X_numerical = df[['total', 'address']].values
X = np.hstack((text_features, X_numerical))
y = df['company']  # Using 'company' as the label (invoice type)

# Scale numerical features
scaler = StandardScaler()

X[:, -2:] = scaler.fit_transform(X[:, -2:])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

```

# Step 3: Train a classifier

```bash
from sklearn.ensemble import RandomForestClassifier

# Initialize the classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier
clf.fit(X_train, y_train)

```

# Step 4: Evaluate the classifier

```bash
from sklearn.metrics import accuracy_score, classification_report

# Predict on the test set
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Print classification report
print(classification_report(y_test, y_pred))

```

# Step 5: Make predictions on new data using Image

```bash
# Function to preprocess new invoice data

def preprocess_new_data(img_path, json_path):
    img_text = extract_text_from_img(img_path)
    json_data = load_json_data(json_path)
    
    # Transform text features
    text_features = vectorizer.transform([img_text]).toarray()
    
    # Extract and encode numerical features, ensuring all inputs are numerical
    total = json_data.get('total', 0.0)
    address = json_data.get('address', '')
    company = json_data.get('company', '')
    
    # If address and company are not needed for numerical features, they should not be included here
    company_encoded = label_encoder.transform([company])[0]
    numerical_features = [[total, company_encoded]]
    
    # Scale numerical features
    numerical_features = scaler.transform(numerical_features)
    
    # Combine text and numerical features
    new_data = np.hstack((text_features, numerical_features))
    
    return new_data

# Path to the new invoice Image and JSON metadata
new_img_path = '/path/to/new/image.jpg'
new_json_path = '/path/to/new/json.json'

# Preprocess new data
new_data = preprocess_new_data(new_img_path, new_json_path)

# Predict the invoice type for the new data
new_prediction = clf.predict(new_data)
print(new_prediction)

```