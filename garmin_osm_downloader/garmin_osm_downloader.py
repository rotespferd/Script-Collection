import os
import sys
import requests
from datetime import datetime

def download_files(urls, root_folder):
    timestamp = datetime.now().strftime('%Y%m%d')
    download_folder = os.path.join(root_folder, timestamp)
    os.makedirs(download_folder, exist_ok=True)

    for url in urls:
        filename = os.path.join(download_folder, os.path.basename(url))
        if os.path.exists(filename):
            print(f"File {filename} already exists, skipping download.")
            continue

        try:
            response = requests.get(url)
            response.raise_for_status()
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded {url} to {filename}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {url}: {e}")

def load_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]
    return urls

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python garmin_osm_downloader.py <root_folder> <url_file>")
        sys.exit(1)

    root_folder = sys.argv[1]
    url_file = sys.argv[2]
    urls = load_urls_from_file(url_file)
    download_files(urls, root_folder)