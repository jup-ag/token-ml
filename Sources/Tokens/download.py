#!/usr/bin/env python3

import argparse
import os
from icrawler.builtin import BingImageCrawler
from icrawler import ImageDownloader

class CustomNameDownloader(ImageDownloader):
    def __init__(self, prefix, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix = prefix
        self.counter = 1

    def get_filename(self, task, default_ext):
        filename = f"{self.prefix}_{self.counter:03d}.{default_ext}"
        self.counter += 1
        return filename

def download_images(query, max_num=100, output_dir='Tokens', prefix=''):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Use a lambda that accepts arbitrary positional and keyword arguments.
    crawler = BingImageCrawler(
        storage={'root_dir': output_dir},
        downloader_cls=lambda *args, **kwargs: CustomNameDownloader(prefix, *args, **kwargs),
        feeder_threads=4,      # Use 4 feeder threads
        parser_threads=4,      # Use 4 parser threads
        downloader_threads=4   # Use 4 downloader threads
    )
    crawler.crawl(keyword=query, max_num=max_num)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Download images for a given search query to a folder.'
    )
    parser.add_argument('query', type=str, help='Search query (e.g., "jupiter token")')
    parser.add_argument('prefix', type=str, help='Prefix for the folder and filenames (e.g., "JUP")')
    parser.add_argument('--max_num', type=int, default=100, help='Maximum number of images to download (default: 100)')
    args = parser.parse_args()
    
    output_folder = args.prefix
    download_images(args.query, max_num=args.max_num, output_dir=output_folder, prefix=args.prefix)