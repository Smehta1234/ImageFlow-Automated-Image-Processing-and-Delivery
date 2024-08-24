import os
import argparse
import zipfile


def zip_directory(input_directory, output_zipfile):
    # Create a ZipFile object
    with zipfile.ZipFile(output_zipfile, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through the input directory
        for root, dirs, files in os.walk(input_directory):
            for file in files:
                file_path = os.path.join(root, file)
                # Write each file into the zip file
                arcname = os.path.relpath(file_path, input_directory)  # Use relative paths
                zipf.write(file_path, arcname)
                print(f"Added {file_path} as {arcname}")


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Zip the contents of a directory')

    # Add arguments
    parser.add_argument('input_directory', type=str, help='Directory containing files to zip')
    parser.add_argument('output_zipfile', type=str, help='Output zip file name (e.g., outputfolder3.zip)')

    # Parse the arguments
    args = parser.parse_args()

    # Call the zip function
    zip_directory(args.input_directory, args.output_zipfile)
