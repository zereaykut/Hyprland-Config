
import os
from pathlib import Path

HOME = str(Path.home())

THEME_MANAGER = f"{HOME}/.config/theme-manager"
WALLPAPERS = f"{HOME}/.config/wallpapers"

CACHE_DIR = f"{HOME}/.cache/theme-manager"
COLOR_SCHEME_CACHE_DIR = f"{CACHE_DIR}/color-schemes"
WALLPAPERS_CACHE_DIR = f"{CACHE_DIR}/wallpapers"


class ColorSys:
    def __init__(self,):
        self.ONE_THIRD = 1.0 / 3.0
        self.ONE_SIXTH = 1.0 / 6.0
        self.TWO_THIRD = 2.0 / 3.0
    
    @staticmethod
    def hex_to_rgb(color):
        """
        Convert a hex color to RGB.
        """
        return tuple(bytes.fromhex(color.strip("#")))

    @staticmethod
    def rgb_to_hex(color):
        """
        Convert an RGB color to hex.
        """
        return "#%02x%02x%02x" % (*color,)

    @staticmethod
    def darken_color(color, amount):
        """
        Darken a hex color.
        """
        color = [int(col * (1 - amount)) for col in ColorSys.hex_to_rgb(color)]
        return ColorSys.rgb_to_hex(color)

    @staticmethod
    def lighten_color(color, amount):
        """
        Lighten a hex color.
        """
        color = [int(col + (255 - col) * amount) for col in ColorSys.hex_to_rgb(color)]
        return ColorSys.rgb_to_hex(color)

    @staticmethod
    def blend_color(color, color2):
        """
        Blend two colors together.
        """
        r1, g1, b1 = ColorSys.hex_to_rgb(color)
        r2, g2, b2 = ColorSys.hex_to_rgb(color2)

        r3 = int(0.5 * r1 + 0.5 * r2)
        g3 = int(0.5 * g1 + 0.5 * g2)
        b3 = int(0.5 * b1 + 0.5 * b2)

        return ColorSys.rgb_to_hex((r3, g3, b3))

    @staticmethod
    def rgb_to_hls(r, g, b):
        """
        Convert RGB to HLS.
        """
        maxc = max(r, g, b)
        minc = min(r, g, b)
        sumc = maxc + minc
        rangec = maxc - minc
        l = sumc / 2.0

        if minc == maxc:
            return 0.0, l, 0.0
        if l <= 0.5:
            s = rangec / sumc
        else:
            s = rangec / (2.0 - maxc - minc)
        rc = (maxc - r) / rangec
        gc = (maxc - g) / rangec
        bc = (maxc - b) / rangec
        if r == maxc:
            h = bc - gc
        elif g == maxc:
            h = 2.0 + rc - bc
        else:
            h = 4.0 + gc - rc
        h = (h / 6.0) % 1.0
        return h, l, s

    @staticmethod
    def _v(m1, m2, h):
        h = h % 1.0
        if h < 1.0 / 6.0:
            return m1 + (m2 - m1) * 6.0 * h
        if h < 0.5:
            return m2
        if h < 2.0 / 3.0:
            return m1 + (m2 - m1) * (2.0 / 3.0 - h) * 6.0
        return m1

    @staticmethod
    def hls_to_rgb(h, l, s):
        """
        Convert HLS to RGB.
        """
        if s == 0.0:
            return l, l, l
        if l <= 0.5:
            m2 = l * (1.0 + s)
        else:
            m2 = l + s - (l * s)
        m1 = 2.0 * l - m2
        return (
            _v(m1, m2, h + self.ONE_THIRD),
            _v(m1, m2, h),
            _v(m1, m2, h - self.ONE_THIRD),
        )

    @staticmethod
    def saturate_color(color, amount):
        """
        Saturate a hex color.
        """
        r, g, b = ColorSys.hex_to_rgb(color)
        r, g, b = [x / 255.0 for x in (r, g, b)]
        h, l, s = ColorSys.rgb_to_hls(r, g, b)
        s = amount
        r, g, b = ColorSys.hls_to_rgb(h, l, s)
        r, g, b = [x * 255.0 for x in (r, g, b)]

        return ColorSys.rgb_to_hex((int(r), int(g), int(b)))

class ImageProcess:
    
    @staticmethod
    def get_images():
        """
        Get images from the wallpaper directory.

        Output:
            images_info[0]: image full path
            images_info[1]: theme name
            images_info[2]: image name with file extension
        """
        themes = os.listdir(WALLPAPERS)
        images_info = []

        for theme in themes:
            images = os.listdir(f"{WALLPAPERS}/{theme}")
            for image in images:
                img_path = f"{WALLPAPERS}/{theme}/{image}"
                images_info.append([img_path, theme, image])

        return images_info

    @staticmethod
    def get_color_scheme_caches(service, overrite=False):
        """
        Process each image and generate color schemes.
        """
        images_info = ImageProcess.get_images()

        for image_info in images_info:
            print(image_info[0])

            os.makedirs(f"{COLOR_SCHEME_CACHE_DIR}/{image_info[1]}/", exist_ok=True)

            output_path = f"{COLOR_SCHEME_CACHE_DIR}/{image_info[1]}/{image_info[2]}.json"
            if not overrite:
                if os.path.exists(output_path):
                    print(f"Exists: {output_path}")
                    continue
            try:
                # self.get_color_scheme(image_info[0], image_info[1], image_info[2])
                colors = service(image_info[0])
                
                theme = image_info[1]
                output_name = image_info[2].rsplit(".", 1)[0]
                FileProcess.save_as_json(theme, output_name, colors)

            except Exception as e:
                error_path = (f"{COLOR_SCHEME_CACHE_DIR}/{image_info[1]}/{image_info[2]}.error")
                with open(error_path, "w") as f:
                    f.writelines("Error:\n")
                    f.writelines(f"{e}:\n")
                    f.writelines(f"{image_info[0]}\n")
                    f.writelines(f"{image_info[1]}\n")
                    f.writelines(f"{image_info[2]}\n")

    @staticmethod
    def get_wall_caches(service, overwrite=False):
        """
        Process each image and generate wallpaper caches.
        """
        images_info = ImageProcess.get_images()

        for image_info in images_info:
            print(image_info[0])

            os.makedirs(f"{WALLPAPERS_CACHE_DIR}/{image_info[1]}/", exist_ok=True)

            output_path = f"{WALLPAPERS_CACHE_DIR}/{image_info[1]}/{image_info[2]}"
            if not overwrite:
                if os.path.exists(output_path):
                    print(f"Exists: {output_path}")
                    continue
            try:
                # self.imagemagick(image_info[0], image_info[1], image_info[2], 640, 360)
                theme = image_info[1]
                cached_image_path = f"{WALLPAPERS_CACHE_DIR}/{theme}/{image_info[2]}"
                service(image_info[0], cached_image_path, 640, 360)
            except Exception as e:
                error_path = (f"{WALLPAPERS_CACHE_DIR}/{image_info[1]}/{image_info[2]}.error")
                with open(error_path, "w") as f:
                    f.writelines("Error:\n")
                    f.writelines(f"{e}:\n")
                    f.writelines(f"{image_info[0]}\n")
                    f.writelines(f"{image_info[1]}\n")
                    f.writelines(f"{image_info[2]}\n")

class FileProcess:
    
    @staticmethod
    def save_as_json(theme, output_name, colors):
        """
        Save the color scheme as a JSON file.
        """
        dictionary = {f"color{i}": color for i, color in enumerate(colors)}

        theme_dir = f"{COLOR_SCHEME_CACHE_DIR}/{theme}"
        with open(f"{theme_dir}/{output_name}.json", "w") as f:
            f.write(json.dumps(dictionary, indent=4))