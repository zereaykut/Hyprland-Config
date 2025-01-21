import os
import re
import subprocess as sp
import shutil
import sys
from pathlib import Path

from .utils import ColorSys


class ImageMagickColorSchemeGenerator:
    """
    Generata a color scheme using imagemagick.
    """
    
    @staticmethod
    def imagemagick(color_count, img, magick_command):
        """
        Call Imagemagick to generate a color scheme.
        """
        flags = ["-resize", "25%", "-colors", str(color_count), "-unique-colors", "txt:-",]
        # flags = ["-depth", "8", "-fuzz", "70%", "+dither", "-kmeans", str(color_count), "-depth", "8", "-format", '"%c"', "histogram:info:",]
        img += "[0]"

        # return sp.run(["magick", img, *flags]).splitlines()
        return sp.check_output([*magick_command, img, *flags], stderr=sp.STDOUT).splitlines()
        # return sp.run(["magick", img, *flags], universal_newlines=True, stdout=sp.PIPE).splitlines()

    @staticmethod
    def has_im():
        """Check to see if the user has im installed."""
        if shutil.which("magick"):
            return ["magick", "convert"]

        if shutil.which("convert"):
            return ["convert"]

        sys.exit(1)

    @staticmethod
    def try_gen_in_range(img, magick_command):
        for i in range(20):
            raw_colors = ImageMagickColorSchemeGenerator.imagemagick(16 + i, img, magick_command)

            if len(raw_colors) > 16:
                break

            if i == 19:
                print("Imagemagick couldn't generate a suitable palette.")

        return raw_colors

    @staticmethod
    def gen_colors(img):
        """Format the output from imagemagick into a list
        of hex colors."""
        magick_command = ImageMagickColorSchemeGenerator.has_im()

        raw_colors = ImageMagickColorSchemeGenerator.try_gen_in_range(img, magick_command)

        try:
            out = [re.search("#.{6}", str(col)).group(0) for col in raw_colors[1:]]
        except AttributeError:
            if magick_command == ["magick", "convert"]:
                print("magick convert failed, using only magick")
                magick_command = ["magick"]
                raw_colors = ImageMagickColorSchemeGenerator.try_gen_in_range(img, magick_command)
                out = [re.search("#.{6}", str(col)).group(0) for col in raw_colors[1:]]

        return out

    @staticmethod
    def adjust(raw_colors, light):
        """
        Adjust the generated colors in a list.
        """

        if light:
            for i in range(len(raw_colors)):
                raw_colors[i] = ColorSys.saturate_color(raw_colors[i], 0.6)
                raw_colors[i] = ColorSys.darken_color(raw_colors[i], 0.5)

            raw_colors[0] = ColorSys.lighten_color(colors[0], 0.85)
            colors[7] = ColorSys.darken_color(colors[0], 0.75)
            colors[8] = ColorSys.darken_color(colors[0], 0.25)
            
            raw_colors[-1] = ColorSys.darken_color(colors[-1], 0.4)
        else:
            raw_colors[0] = ColorSys.darken_color(raw_colors[0], 0.50)
            raw_colors[1] = ColorSys.darken_color(raw_colors[1], 0.30)
            raw_colors[2] = ColorSys.darken_color(raw_colors[1], 0.20)
            raw_colors[3] = ColorSys.darken_color(raw_colors[1], 0.20)
            
            raw_colors[-4] = ColorSys.darken_color(raw_colors[-4], 0.10)
            raw_colors[-3] = ColorSys.blend_color(raw_colors[-3], "#EEEEEE")
            raw_colors[-2] = ColorSys.lighten_color(raw_colors[-2], 0.20)
            raw_colors[-1] = ColorSys.lighten_color(raw_colors[-1], 0.50)

        return raw_colors

    @staticmethod
    def run(img, light=False):
        raw_colors = ImageMagickColorSchemeGenerator.gen_colors(img)
        adjusted_colors = ImageMagickColorSchemeGenerator.adjust(raw_colors, light)
        return adjusted_colors

class ImageMagickWallpaperCacheGenerator:
    """
    Generate a wallpaper cache using imagemagick.
    """

    @staticmethod
    def imagemagick(img, cached_image_path, width, height):
        """
        Call Imagemagick to generate a color scheme.
        """
        

        flags = ["-strip", "-thumbnail", f"{width}x{height}^", "-gravity", "center", "-extent", f"{width}x{height}", cached_image_path,]
        img += "[0]"
        sp.check_output(["magick", img, *flags])
    
    @staticmethod
    def run(img, cached_image_path, width, height):
        ImageMagickWallpaperCacheGenerator.imagemagick(img, cached_image_path, width, height)



