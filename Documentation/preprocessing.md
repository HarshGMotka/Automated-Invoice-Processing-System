Enhancing an image for better OCR (Optical Character Recognition) results involves several steps to preprocess the image, such as resizing, denoising, binarizing, and applying contrast adjustments.

1. Install the required libraries if you haven't already:

```bash
pip install opencv-python pillow numpy
```

# Explanation:
1. **Loading the Image**: The image is loaded in grayscale mode.
2. **Resizing**: The image is resized to double its original size to make the text more readable.
3. **Denoising**: The fastNlMeansDenoising function is used to reduce noise in the image.
4. **Binarization**: The image is binarized using Otsu's thresholding method to separate the text from the background.
5. **Contrast Adjustment**: The contrast of the image is increased using the ImageEnhance.Contrast function from the PIL library.
6. **Saving the Enhanced Image**: The final enhanced image is saved to the specified output path.

This preprocessing should significantly improve the OCR results.