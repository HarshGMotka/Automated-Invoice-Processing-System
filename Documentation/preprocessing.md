Enhancing an image for better OCR (Optical Character Recognition) results involves several steps to preprocess the image, such as resizing, denoising, binarizing, and applying contrast adjustments.

Sample [Images](../dataset/images/) are available for testing of image quality enhancement.

1. Install the required libraries if you haven't already:

```bash
pip install opencv-python pillow numpy
```

2. Use the [code](../preprocessing/preprocessing.py) to enhance the image quality.


# Explanation:
1. **Loading the Image**: The image is loaded in grayscale mode.
2. **Resizing**: The image is resized to double its original size to make the text more readable.
3. **Denoising**: The fastNlMeansDenoising function is used to reduce noise in the image.
4. **Binarization**: The image is binarized using Otsu's thresholding method to separate the text from the background.
5. **Contrast Adjustment**: The contrast of the image is increased using the **ImageEnhance.Contrast**. Contrast function from the PIL library.
6. **Brightness Adjustment**: 
    - The Brightness Adjustment is used to adjust the brightness of the image using **ImageEnhance.Brightness**.
    - The enhance method is called with a factor of 1.5, which increases the brightness by 50%. You can adjust this value according to your needs.
7. **Saving the Enhanced Image**: The final enhanced image is saved to the specified output path.

This preprocessing should significantly improve the OCR results.
