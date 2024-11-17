import os
import argparse
import subprocess as sp
from pathlib import Path

from services.imagemagick import ImageMagickWallpaperCacheGenerator

def main():
    """
    python wall_cache.py --service <parameter>
        << --service >>
            imagemagick: use imagemagick as backend service
            pillow: use pillow as backend service
        << --overwrite >>
            True: overwrite cached wallpapers
            False: skip cached wallpapers
    """

    parser = argparse.ArgumentParser(description="Color Scheme Generator.")
    parser.add_argument( "-s", "--service", help="Backend service to use color scheme generation, options: imagemagick & pillow", required=True,)
    parser.add_argument( "-o", "--overwrite", help="Overwrite existing cached wallpapers, options: True or False", required=False,)

    args = parser.parse_args()
    
    service = args.service
    overwrite = args.overwrite

    try:
        overwrite = bool(overwrite)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit("overwrite should be True or False")

    if service == "imagemagick":
        generator = ImageMagickWallpaperCacheGenerator()
        if overwrite:
            generator.process_images(overwrite=True)
        else:
            generator.process_images()
        
    elif service == "pillow":
        sys.exit("Not implemented yet")
    else:
        sys.exit("Invalid service chosen.\nAvailable service options:\niamgemagick\npillow")

if __name__ == "__main__":
    main()  