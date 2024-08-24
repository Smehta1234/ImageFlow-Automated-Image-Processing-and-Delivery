import os
import argparse
import cv2


def convert_images_to_grayscale(input_directory, output_directory):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate through all files in the input directory
    for filename in os.listdir(input_directory):
        file_path = os.path.join(input_directory, filename)

        if os.path.isdir(file_path):
            print(f"Skipping directory: {file_path}")
            continue

        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):  # Supported image formats
            print(f"Processing file: {file_path}")

            # Read the image using OpenCV
            img = cv2.imread(file_path)
            if img is None:
                print(f"Skipping {filename}: Unable to read the image.")
                continue

            # Convert the image to grayscale
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Save the grayscale image to the output directory
            save_path = os.path.join(output_directory, filename)
            cv2.imwrite(save_path, gray_img)
            print(f"Converted {filename} to grayscale and saved to {save_path}")
        else:
            print(f"Skipping {filename}: Unsupported file format.")


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Convert images to grayscale using OpenCV')

    # Add arguments
    parser.add_argument('input_directory', type=str, help='Directory containing images to convert')
    parser.add_argument('output_directory', type=str, help='Directory to save the grayscale images')

    # Parse the arguments
    args = parser.parse_args()

    # Convert images to grayscale
    convert_images_to_grayscale(args.input_directory, args.output_directory)

