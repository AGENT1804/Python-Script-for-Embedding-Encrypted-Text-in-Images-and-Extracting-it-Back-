Image Steganography with Text Encryption (Python)

This Python script provides functionalities for hiding text messages within images using steganography techniques and encrypting the hidden message for additional security.

Features:

* Embed text messages into images (least significant bit modification)
* Encrypt/decrypt text messages using XOR encryption
* Extract hidden text messages from images

Requirements:

* Python 3.x
* OpenCV library (installation instructions: [https://opencv.org/](https://opencv.org/))

Usage:

1. Install OpenCV library.
2. Run the script (`python image_steganography.py`).
3. Choose an option:
    1. Encrypt and embed text into an image:**
      * Provide the path to the text file containing the message.
      * Provide the path to the image file where the message will be hidden.
      * Provide the desired filename (with .png or .jpg extension) to save the modified image.
    2. Extract and decrypt text from an image:**
      * Provide the path to the image file containing the hidden message.
      * Enter the length of the embedded text message (same length used during embedding).
      * (Optional) Provide a filename to save the extracted and decrypted text.
Example:


Choose an option:
1. Encrypt and embed text into an image
2. Extract and decrypt text from an image
Enter your choice (1 or 2): 1

Enter the path to the input text file: secret_message.txt
Enter the path to the input image file: image.jpg
Enter the path to save the output image (with extension .png or .jpg): output_image.png

Text has been successfully embedded in the image.


Note:

* This script demonstrates a basic implementation of steganography and encryption. The hidden message size is limited by the image size.
* Ensure you use the same text length during extraction as used during embedding.

Disclaimer:

This script is for educational purposes only. Steganography techniques might not be suitable for highly confidential information.
