import cv2
import numpy as np
from PIL import Image, ImageEnhance

def enhance_image_for_ocr(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Resize the image to make it larger
    image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Denoise the image
    image = cv2.fastNlMeansDenoising(image, None, 30, 7, 21)

    # Binarize the image
    _, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Convert back to PIL for further enhancements
    image_pil = Image.fromarray(image)

    # Increase contrast
    enhancer = ImageEnhance.Contrast(image_pil)
    image_pil = enhancer.enhance(2)

    # Adjust the brightness
    brightness_enhancer = ImageEnhance.Brightness(image_pil)
    image_pil = brightness_enhancer.enhance(1.5)

    # Save the enhanced image
    image_pil.save(output_path)

    return output_path

# Example usage
input_image_path = '/path/to/input/image/input_image.jpg'
output_image_path = '/path/to/output/image/enhanced_image.jpg'

enhanced_image_path = enhance_image_for_ocr(input_image_path, output_image_path)

print(f'Enhanced image saved at: {enhanced_image_path}')

