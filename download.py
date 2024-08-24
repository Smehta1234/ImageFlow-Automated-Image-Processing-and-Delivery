import argparse
from bing_image_downloader import downloader

def download_images(limit, keywords, output_directory):
    downloader.download(keywords, limit=limit, output_dir=output_directory, adult_filter_off=True, force_replace=False, timeout=60)
    print(f"Downloaded {limit} images of '{keywords}' into {output_directory}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download images using bing-image-downloader')
    parser.add_argument('limit', type=int, help='Number of images to download')
    parser.add_argument('keywords', type=str, help='Search keywords')
    parser.add_argument('output_directory', type=str, help='Output directory to save images')
    args = parser.parse_args()

    download_images(args.limit, args.keywords, args.output_directory)
