import os
import sys
import json
import requests
import feedparser
from concurrent.futures import ThreadPoolExecutor

def download_podcast(url, dest_folder):
    response = requests.get(url, stream=True)
    filename = os.path.join(dest_folder, url.split('/')[-1])
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print(f"Downloaded: {filename}")

def main(json_path):
    with open(json_path, 'r') as f:
        config = json.load(f)
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = []
        for feed_url, dest_folder in config.items():
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            
            feed = feedparser.parse(feed_url)
            for entry in feed.entries:
                podcast_url = entry.enclosures[0].href
                podcast_filename = os.path.join(dest_folder, podcast_url.split('/')[-1])
                if not os.path.exists(podcast_filename):
                    futures.append(executor.submit(download_podcast, podcast_url, dest_folder))
                else:
                    print(f"File {podcast_filename} already exists, skipping download.")
        
        for future in futures:
            future.result()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python podcast_archiver.py <path_to_json>")
        sys.exit(1)
    
    json_path = sys.argv[1]
    main(json_path)