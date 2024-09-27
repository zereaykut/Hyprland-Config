import sys
import os
import re
import subprocess as sp
import json

class WallpaperCacheGenerator:
    def __init__(self, user):
        self.user = user
        self.base_dir = f"/home/{self.user}/.cache/theme-manager/wallpapers"
        self.wallpaper_dir = f"/home/{self.user}/.config/wallpapers"

    def imagemagick(self, img, theme, img_cache, width, height):
        """
        Call Imagemagick to generate a color scheme.
        """
        cache_dir = f"{self.base_dir}/{theme}"
        os.makedirs(cache_dir, exist_ok=True)

        flags = ["-strip", "-thumbnail", f"{width}x{height}^", "-gravity", "center", "-extent", f"{width}x{height}", f"{cache_dir}/{img_cache}"]
        img += "[0]"
        sp.check_output(["magick", img, *flags])

    def get_images(self):
        """
        Get images from the wallpaper directory.
        """
        themes = os.listdir(self.wallpaper_dir)
        images_info = []

        for theme in themes:
            images = os.listdir(f"{self.wallpaper_dir}/{theme}")
            for image in images:
                img_path = f"{self.wallpaper_dir}/{theme}/{image}"
                images_info.append([img_path, theme, image])

        return images_info        

    def process_images(self):
        """
        Process each image and generate wallpaper caches.
        """
        images_info = self.get_images()

        for image_info in images_info:
            print(image_info[0])

            output_path = f"{self.base_dir}/{image_info[1]}/{image_info[2]}"
            if os.path.exists(output_path):
                print(f"Exists: {output_path}")
            else:
                try:
                    self.imagemagick(image_info[0], image_info[1], image_info[2], 640, 360)
                except Exception as e:
                    error_path = f"{self.base_dir}/{image_info[1]}/{image_info[2]}.error"
                    with open(error_path, "w") as f:
                        f.writelines("Error:\n")
                        f.writelines(f"{e}:\n")
                        f.writelines(f"{image_info[0]}\n")
                        f.writelines(f"{image_info[1]}\n")
                        f.writelines(f"{image_info[2]}\n")


if __name__ == "__main__":
    user = sp.run("whoami", shell=True, capture_output=True, text=True).stdout.strip()
    generator = WallpaperCacheGenerator(user)
    generator.process_images()
