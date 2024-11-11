import json
import os
import re
import subprocess as sp
from pathlib import Path

class ColorSchemeGenerator:
    ONE_THIRD = 1.0 / 3.0
    ONE_SIXTH = 1.0 / 6.0
    TWO_THIRD = 2.0 / 3.0

    def __init__(self, user):
        self.home = str(Path.home())
        self.base_dir = f"{self.home}/.cache/theme-manager/color-schemes"
        self.wallpaper_dir = f"/home/{self.user}/.config/wallpapers"

    def imagemagick(self, color_count, img):
        """
        Call Imagemagick to generate a color scheme.
        """
        # flags = ["-resize", "25%", "-colors", str(color_count), "-unique-colors", "txt:-"]
        flags = [
            "-depth",
            "8",
            "-fuzz",
            "70%",
            "+dither",
            "-kmeans",
            str(color_count),
            "-depth",
            "8",
            "-format",
            '"%c"',
            "histogram:info:",
        ]
        img += "[0]"

        return sp.check_output(["magick", img, *flags]).splitlines()

    def gen_colors(self, img):
        """
        Format the output from imagemagick into a list of hex colors.
        """
        for i in range(11):
            raw_colors = self.imagemagick(6 + i, img)

            if len(raw_colors) > 6:
                break

            if i == 16:
                print("Imagemagick couldn't generate a suitable palette.")

            print(
                f"Imagemagick couldn't generate a palette. Trying a larger palette size {6 + i}"
            )

        # return [re.search("#.{6}", str(col)).group(0) for col in raw_colors[1:]]
        raw_colors = [
            match.group(0) for i in raw_colors if (match := re.search(r"#.{6}", str(i)))
        ]
        return raw_colors

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
        color = [int(col * (1 - amount)) for col in self.hex_to_rgb(color)]
        return self.rgb_to_hex(color)

    @staticmethod
    def lighten_color(color, amount):
        """
        Lighten a hex color.
        """
        color = [int(col + (255 - col) * amount) for col in self.hex_to_rgb(color)]
        return self.rgb_to_hex(color)

    @staticmethod
    def blend_color(color, color2):
        """
        Blend two colors together.
        """
        r1, g1, b1 = self.hex_to_rgb(color)
        r2, g2, b2 = self.hex_to_rgb(color2)

        r3 = int(0.5 * r1 + 0.5 * r2)
        g3 = int(0.5 * g1 + 0.5 * g2)
        b3 = int(0.5 * b1 + 0.5 * b2)

        return self.rgb_to_hex((r3, g3, b3))

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
            self._v(m1, m2, h + self.ONE_THIRD),
            self._v(m1, m2, h),
            self._v(m1, m2, h - self.ONE_THIRD),
        )

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
    def saturate_color(color, amount):
        """
        Saturate a hex color.
        """
        r, g, b = self.hex_to_rgb(color)
        r, g, b = [x / 255.0 for x in (r, g, b)]
        h, l, s = self.rgb_to_hls(r, g, b)
        s = amount
        r, g, b = self.hls_to_rgb(h, l, s)
        r, g, b = [x * 255.0 for x in (r, g, b)]

        return self.rgb_to_hex((int(r), int(g), int(b)))

    @staticmethod
    def adjust(self, raw_colors, light):
        """
        Adjust the generated colors in a list.
        """

        if light:
            for i in range(len(raw_colors)):
                raw_colors[i] = self.saturate_color(raw_colors[i], 0.5)

            raw_colors[0] = self.lighten_color(colors[0], 0.85)
            raw_colors[-1] = self.darken_color(colors[-1], 0.4)
        else:
            raw_colors[0] = self.darken_color(raw_colors[0], 0.50)
            raw_colors[1] = self.darken_color(raw_colors[1], 0.10)
            raw_colors[-3] = self.blend_color(raw_colors[-3], "#EEEEEE")
            raw_colors[-2] = self.darken_color(raw_colors[-2], 0.30)
            raw_colors[-1] = self.blend_color(raw_colors[-1], "#EEEEEE")

        return raw_colors

    def save_as_json(self, theme, output_name, raw_colors):
        """
        Save the color scheme as a JSON file.
        """
        dictionary = {
            "main-bg": raw_colors[0],
            "main-fg": raw_colors[-1],
            "wb-act-bg": raw_colors[1],
            "wb-act-fg": raw_colors[-2],
            "wb-hvr-bg": raw_colors[2],
            "wb-hvr-fg": raw_colors[-3],
        }

        theme_dir = f"{self.base_dir}/{theme}"
        os.makedirs(theme_dir, exist_ok=True)

        with open(f"{theme_dir}/{output_name}.json", "w") as f:
            f.write(json.dumps(dictionary, indent=4))

    def get_color_scheme(self, img, theme, output_name, light=False):
        """
        Generate and save the color scheme.
        """
        raw_colors = self.gen_colors(img)
        adjusted_colors = self.adjust(raw_colors, light)
        self.save_as_json(theme, output_name, adjusted_colors)

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
                images_info.append([img_path, theme, image.rsplit(".", 1)[0]])

        return images_info

    def process_images(self):
        """
        Process each image and generate color schemes.
        """
        images_info = self.get_images()

        for image_info in images_info:
            print(image_info[0])

            output_path = f"{self.base_dir}/{image_info[1]}/{image_info[2]}.json"
            if os.path.exists(output_path):
                print(f"Exists: {output_path}")
            else:
                try:
                    self.get_color_scheme(image_info[0], image_info[1], image_info[2])
                except Exception as e:
                    error_path = (
                        f"{self.base_dir}/{image_info[1]}/{image_info[2]}.error"
                    )
                    with open(error_path, "w") as f:
                        f.writelines("Error:\n")
                        f.writelines(f"{e}:\n")
                        f.writelines(f"{image_info[0]}\n")
                        f.writelines(f"{image_info[1]}\n")
                        f.writelines(f"{image_info[2]}\n")


if __name__ == "__main__":
    generator = ColorSchemeGenerator()
    generator.process_images()
