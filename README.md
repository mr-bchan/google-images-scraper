```
usage: scrape_images.py [-h] --keywords KEYWORDS --sources SOURCES
                        [--image_directory IMAGE_DIRECTORY]
                        [--n_images N_IMAGES] [--cleanup CLEANUP]
                        [--metadata METADATA]

Download images given topics and URL sources.

optional arguments:
  -h, --help            show this help message and exit
  --keywords KEYWORDS   keywords file path
  --sources SOURCES     urls file path
  --image_directory IMAGE_DIRECTORY
                        downloads/ subfolder
  --n_images N_IMAGES   number of images per topic per source
  --cleanup CLEANUP     if remove download and logs folder
  --metadata METADATA   if save metadata file
  
```
Sample script:
```
python scripts/scrape_images.py 
  --cleanup TRUE
  --keywords 'data/keywords.txt' 
  --sources 'data/image_sources.txt' 
  --metadata TRUE
```
