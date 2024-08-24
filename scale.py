import os
import argparse
from PIL import Image


def scale_images(scale_percentage, input_directory, output_directory):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate through all files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):  # Supported image formats
            img_path = os.path.join(input_directory, filename)
            print(f"Processing file: {img_path}")

            # Open the image using PIL
            img = Image.open(img_path)

            # Calculate new dimensions
            width, height = img.size
            new_width = int(width * scale_percentage / 100)
            new_height = int(height * scale_percentage / 100)

            # Scale the image using the updated LANCZOS resampling filter
            scaled_img = img.resize((new_width, new_height), Image.LANCZOS)

            # Save the scaled image to the output directory
            save_path = os.path.join(output_directory, filename)
            scaled_img.save(save_path)
            print(f"Scaled {filename} to {scale_percentage}% of original size and saved to {save_path}")
        else:
            print(f"Skipping {filename}: Unsupported file format.")


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Scale images by a percentage using PIL')

    # Add arguments
    parser.add_argument('scale_percentage', type=str, help='Scaling percentage (e.g., "50%" for 50% of original size)')
    parser.add_argument('input_directory', type=str, help='Directory containing images to scale')
    parser.add_argument('output_directory', type=str, help='Directory to save the scaled images')

    # Parse the arguments
    args = parser.parse_args()

    # Convert scale_percentage to a number and remove the '%' sign
    scale_percentage = float(args.scale_percentage.strip('%'))

    # Call the scaling function
    scale_images(scale_percentage, args.input_directory, args.output_directory)
