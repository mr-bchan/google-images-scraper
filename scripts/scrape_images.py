import os
import shutil
import datetime
import argparse
import sys
sys.path.insert(0, '.')

from scraper import image as image_scraper
from scripts import build_metadata

def remove_folders(folders):
    print('=========================================')
    for folder in folders:
        print('Removing folder: {}'.format(folder))
        if os.path.exists(folder):
            shutil.rmtree(folder)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Download images given topics and URL sources.')

    parser.add_argument("--keywords", help='keywords file path', required=True)
    parser.add_argument("--sources", help='urls file path', required=True)

    parser.add_argument("--image_directory", help='downloads/ subfolder', default='')
    parser.add_argument("--n_images", help='number of images per topic per source', default=15)
    parser.add_argument("--cleanup", help='if remove download and logs folder', default='false')
    parser.add_argument("--metadata", help='if save metadata file', default='false')

    args = parser.parse_args()

    # Remove output folders
    # downloads - images
    # logs - metadata

    if args.cleanup.lower() == 'true':
        remove_folders(['downloads', 'logs'])

    # Retrieve list of topics from config folder
    keyword_file_path = os.path.join(args.keywords)
    image_source_file_path = os.path.join(args.sources)
    n_images = args.n_images
    image_directory = args.image_directory

    with open(keyword_file_path, 'r') as infile:
        keywords = infile.readlines()

    with open(image_source_file_path, 'r') as infile:
        image_sources = infile.readlines()

    keywords = image_scraper.clean_keyword(keywords)
    image_sources = image_scraper.clean_source(image_sources)

    start_time = datetime.datetime.now()

    image_scraper.scrape(keywords=keywords,
                         sources=image_sources,
                         n_images=n_images,
                         image_directory=image_directory)

    end_time = datetime.datetime.now()
    elapsedTime = end_time - start_time

    print()
    print()
    print('Number of minutes and seconds elapsed: {}'.format(divmod(elapsedTime.total_seconds(), 60)))
    print()
    print()

    if args.metadata.lower() == 'true':
        print('Saving metadata file to folder: {}'.format(image_directory))
        build_metadata.build_metadata(logs_folder='logs', output_folder=image_directory)
