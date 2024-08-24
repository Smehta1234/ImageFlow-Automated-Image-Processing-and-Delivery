import os
import argparse
import shutil

def clean_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Automate the process of downloading, processing, and sending images via email.')

    # Add arguments
    parser.add_argument('--num_images', type=int, required=True, help='Number of images to download')
    parser.add_argument('--keywords', type=str, required=True, help='Search keywords for image download')
    parser.add_argument('--scale_percentage', type=str, required=True, help='Scaling percentage (e.g., "5%" for 5% of original size)')
    parser.add_argument('--receiver_email', type=str, required=True, help='Receiver email address')
    parser.add_argument('--output_folder1', type=str, default='outputFolder1', help='Output folder for downloaded images')
    parser.add_argument('--output_folder2', type=str, default='outputFolder2', help='Output folder for grayscale images')
    parser.add_argument('--output_folder3', type=str, default='outputFolder3', help='Output folder for scaled images')
    parser.add_argument('--zip_file', type=str, default='outputFolder3.zip', help='Name of the zip file')

    # Parse the arguments
    args = parser.parse_args()

    # Clean up directories before starting
    clean_directory(args.output_folder1)
    clean_directory(args.output_folder2)
    clean_directory(args.output_folder3)

    if os.path.exists(args.zip_file):
        os.remove(args.zip_file)

    # Step 1: Download images using the download.py script
    os.system(f"python download.py {args.num_images} '{args.keywords}' {args.output_folder1}")

    # Adjusted keyword folder search to handle quotes in the folder name
    keyword_folder = os.path.join(args.output_folder1, f"'{args.keywords}'")

    if not os.path.exists(keyword_folder):
        print(f"Error: Could not find the subdirectory for the keyword '{args.keywords}' in {args.output_folder1}.")
        return

    # Step 2: Convert the downloaded images to grayscale using the convert_to_grey_scale.py script
    os.system(f"python convert_to_grey_scale.py {keyword_folder} {args.output_folder2}")

    # Step 3: Scale the grayscale images using the scale.py script
    os.system(f"python scale.py {args.scale_percentage} {args.output_folder2} {args.output_folder3}")

    # Step 4: Zip the scaled images using the zip.py script
    os.system(f"python zip.py {args.output_folder3} {args.zip_file}")

    # Step 5: Send the zipped file via email using the sendToEmail.py script
    os.system(f"python sendtoemailid.py {args.zip_file} {args.receiver_email}")

if __name__ == "__main__":
    main()
