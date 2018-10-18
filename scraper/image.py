"""
Google Images scraper given:
1. keywords (topics)
2. sources (URLs)
3. n number of image per topic per source
"""

import os
from nltk.corpus import stopwords
from google_images_download import google_images_download   #importing the library


# Load stop words
stop_words = stopwords.words('english')


def scrape(keywords, sources, image_directory, n_images=5):
    response = google_images_download.googleimagesdownload()
    for keyword in keywords:
        for source in sources:
            print('=========================================')
            print('site:{} "{}"'.format(source, keyword))
            print('=========================================')

            arguments = {"keywords": 'site:{} "{}"'.format(source, keyword),
                         "limit": n_images,
                         "print_urls": True,
                         "extract_metadata": True,
                         "image_directory": os.path.join(image_directory, keyword,'images'),
                         "specific_site": source}  # creating list of arguments

            paths = response.download(arguments)  # passing the arguments to the function
            print(paths)  # printing absolute paths of the downloaded images

# preprocess topic names:
# lowercase,remove stop words, strip, etc.
def clean_keyword(keywords):
    clean_keywords = []
    for keyword in keywords:
        keyword = keyword.strip().lower()

        tokens = keyword.split()
        keyword = [word for word in tokens if word not in stop_words]
        keyword = ' '.join(keyword).replace(',', '+')
        clean_keywords.append(keyword)
    return clean_keywords


def clean_source(sources):
    import re
    http_regex = re.compile(r"https?://(www\.)?")
    clean_sources = []
    for source in sources:
        c_source = http_regex.sub('', source).strip().strip('/').split('/')[0]
        clean_sources.append(c_source)
    return clean_sources
