import subprocess as sp

from wall_cache import WallpaperCacheGenerator


class WallpaperCacheGeneratorOW(WallpaperCacheGenerator):
    def process_images(self):
        """
        Process each image and generate wallpaper caches.
        Overwrite existing wallpaper caches.
        """
        images_info = self.get_images()

        for image_info in images_info:
            print(image_info[0])

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
    generator = WallpaperCacheGeneratorOW(user)
    generator.process_images()
