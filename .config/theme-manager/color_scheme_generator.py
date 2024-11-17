import os
import argparse
import subprocess as sp
import sys

from services.imagemagick import ImageMagick

def main():
    """
    python color_scheme_generator.py --service <parameter>
        << --service >>
            imagemagick: use imagemagick as backend service
            colorthief: use colorthief as backend service
        << --overwrite >>
            True: overwrite existing colorschemes
            False: skip existing color schemes
    """

    parser = argparse.ArgumentParser(description="Color Scheme Generator.")
    parser.add_argument( "-s", "--service", help="Backend service to use color scheme generation, options: imagemagick & colorthief", required=True,)
    parser.add_argument( "-o", "--overwrite", help="Overwrite existing color schemes, options: True or False", required=False,)

    args = parser.parse_args()
    
    service = args.service
    overwrite = args.overwrite

    try:
        overwrite = bool(overwrite)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit("overwrite should be True or False")

    if service == "imagemagick":
        generator = ImageMagick()
        if overwrite:
            generator.process_images(overrite=True)
        else:
            generator.process_images()
        
    elif service == "colorthief":
        sys.exit("Not implemented yet")
    else:
        sys.exit("Invalid service chosen.\nAvailable service options:\niamgemagick\ncolorthief")

if __name__ == "__main__":
    main()    
