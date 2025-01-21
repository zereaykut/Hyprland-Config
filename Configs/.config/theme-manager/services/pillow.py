
import os, sys
from PIL import Image

from .utils import ColorSys

class PillowkWallpaperCacheGenerator:

    @staticmethod
    def gen_cache(img, cached_image_path, width, height):
        try:
            image = Image.open(img)
            thumbnail_size = (width, height)
            image.thumbnail(thumbnail_size)
            image.save("example_thumbnail.png")
        except Exception as e:
            print(f"Couldn't generate a thumbnail for {img} error: {e}")