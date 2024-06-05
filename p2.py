import os

import cv2
import numpy as np


# Function to XOR encrypt/decrypt text
def xor_encrypt_decrypt(text, key):
    return ''.join(chr(ord(c) ^ ord(key)) for c in text)

# Function to read a file into a string
def read_file(filename):
    try:
        with open(filename, 'rb') as file:
            return file.read().decode()
    except Exception as e:
        print(f"Failed to open file: {filename}, error: {e}")
        return ""

# Function to write a string to a file
def write_file(filename, data):
    try:
        with open(filename, 'wb') as file:
            file.write(data.encode())
    except Exception as e:
        print(f"Failed to open file: {filename}, error: {e}")

# Function to embed text into an image
def embed_text_in_image(text, image):
    if image.shape[2] < 3:
        print("Image must have at least 3 channels")
        return

    if len(text) > image.shape[0] * image.shape[1]:
        print("Text is too large to embed in the image")
        return

    text_index = 0
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if text_index < len(text):
                image[i, j, 0] = ord(text[text_index])
                text_index += 1
            else:
                break
        if text_index >= len(text):
            break

# Function to extract text from an image
def extract_text_from_image(image, text_length):
    extracted_text = []
    text_index = 0
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if text_index < text_length:
                extracted_text.append(chr(image[i, j, 0]))
                text_index += 1
            else:
                break
        if text_index >= text_length:
            break
    return ''.join(extracted_text)

def main():
    print("Choose an option:")
    print("1. Encrypt and embed text into an image")
    print("2. Extract and decrypt text from an image")
    choice = input("Enter your choice (1 or 2): ")

    key = 'K'  # Encryption key

    if choice == '1':
        input_filename = input("Enter the path to the input text file: ")
        image_filename = input("Enter the path to the input image file: ")
        output_image_filename = input("Enter the path to save the output image (with extension .png or .jpg): ")

        # Check if files exist
        if not os.path.isfile(input_filename):
            print(f"Input text file does not exist: {input_filename}")
            return
        if not os.path.isfile(image_filename):
            print(f"Input image file does not exist: {image_filename}")
            return

        # Ensure output file has a valid extension
        valid_extensions = ['.png', '.jpg', '.jpeg']
        if not any(output_image_filename.lower().endswith(ext) for ext in valid_extensions):
            print("Output file must have a valid extension: .png, .jpg, or .jpeg")
            return

        # Read the file to encrypt
        file_content = read_file(input_filename)

        if not file_content:
            print("File content is empty or failed to read file.")
            return

        # Encrypt the file content
        encrypted_text = xor_encrypt_decrypt(file_content, key)

        # Load the image
        image = cv2.imread(image_filename)
        if image is None:
            print("Could not open or find the image")
            return

        # Embed the encrypted text into the image
        embed_text_in_image(encrypted_text, image)

        # Save the image with embedded text
        if not cv2.imwrite(output_image_filename, image):
            print("Failed to save the image.")
            return

        print("Text has been successfully embedded in the image.")

    elif choice == '2':
        image_filename = input("Enter the path to the input image file: ")
        output_filename = input("Enter the path to save the decrypted output text file: ")

        # Check if file exists
        if not os.path.isfile(image_filename):
            print(f"Input image file does not exist: {image_filename}")
            return

        # Load the image
        image = cv2.imread(image_filename)
        if image is None:
            print("Could not open or find the image")
            return

        # Determine the length of the embedded text
        text_length = int(input("Enter the length of the embedded text: "))

        # Extract the text from the image
        extracted_text = extract_text_from_image(image, text_length)

        # Decrypt the extracted text
        decrypted_text = xor_encrypt_decrypt(extracted_text, key)

        # Write the decrypted text to a file
        write_file(output_filename, decrypted_text)

        # Print the decrypted text to the terminal
        print("Decrypted text:")
        print(decrypted_text)

    else:
        print("Invalid choice. Please select either 1 or 2.")

if __name__ == "__main__":
    main()
