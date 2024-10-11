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

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python garmin_osm_downloader.py <root_folder> <url1> <url2> ... <urlN>")
        sys.exit(1)

    root_folder = sys.argv[1]
    urls = sys.argv[2:]
    download_files(urls, root_folder)