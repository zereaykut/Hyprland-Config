import sys
import os
import re
import subprocess as sp
import json

def imagemagick(color_count, img):
    """
    Call Imagemagick to generate a color scheme.
    """
    flags = ["-resize", "25%", "-colors", str(color_count), "-unique-colors", "txt:-"]
    img += "[0]"

    return sp.check_output(["magick", img, *flags]).splitlines()

def gen_colors(img):
    """
    Format the output from imagemagick into a list of hex colors.
    """

    for i in range(0, 20, 1):
        raw_colors = imagemagick(16 + i, img)

        if len(raw_colors) > 16:
            break

        if i == 19:
            print("Imagemagick couldn't generate a suitable palette.")
            sys.exit(1)

        else:
            print("Imagemagick couldn't generate a palette.")
            print("Trying a larger palette size %s", 16 + i)

    return [re.search("#.{6}", str(col)).group(0) for col in raw_colors[1:]]

def hex_to_rgb(color):
    """
    Convert a hex color to rgb.
    """
    return tuple(bytes.fromhex(color.strip("#")))

def rgb_to_hex(color):
    """
    Convert an rgb color to hex.
    """
    return "#%02x%02x%02x" % (*color,)


def darken_color(color, amount):
    """
    Darken a hex color.
    """
    color = [int(col * (1 - amount)) for col in hex_to_rgb(color)]
    return rgb_to_hex(color)


def lighten_color(color, amount):
    """
    Lighten a hex color.
    """
    color = [int(col + (255 - col) * amount) for col in hex_to_rgb(color)]
    return rgb_to_hex(color)


def blend_color(color, color2):
    """
    Blend two colors together.
    """
    r1, g1, b1 = hex_to_rgb(color)
    r2, g2, b2 = hex_to_rgb(color2)

    r3 = int(0.5 * r1 + 0.5 * r2)
    g3 = int(0.5 * g1 + 0.5 * g2)
    b3 = int(0.5 * b1 + 0.5 * b2)

    return rgb_to_hex((r3, g3, b3))

ONE_THIRD = 1.0/3.0
ONE_SIXTH = 1.0/6.0
TWO_THIRD = 2.0/3.0

def rgb_to_hls(r, g, b):
    """
    Convert rgb to hls
    """
    maxc = max(r, g, b)
    minc = min(r, g, b)
    sumc = (maxc+minc)
    rangec = (maxc-minc)
    l = sumc/2.0
    if minc == maxc:
        return 0.0, l, 0.0
    if l <= 0.5:
        s = rangec / sumc
    else:
        s = rangec / (2.0-maxc-minc)  # Not always 2.0-sumc: gh-106498.
    rc = (maxc-r) / rangec
    gc = (maxc-g) / rangec
    bc = (maxc-b) / rangec
    if r == maxc:
        h = bc-gc
    elif g == maxc:
        h = 2.0+rc-bc
    else:
        h = 4.0+gc-rc
    h = (h/6.0) % 1.0
    return h, l, s

def hls_to_rgb(h, l, s):
    """
    Convert hls to rgb.
    """
    if s == 0.0:
        return l, l, l
    if l <= 0.5:
        m2 = l * (1.0+s)
    else:
        m2 = l+s-(l*s)
    m1 = 2.0*l - m2
    return (_v(m1, m2, h+ONE_THIRD), _v(m1, m2, h), _v(m1, m2, h-ONE_THIRD))

def saturate_color(color, amount):
    """
    Saturate a hex color.
    """
    r, g, b = hex_to_rgb(color)
    r, g, b = [x / 255.0 for x in (r, g, b)]
    h, l, s = rgb_to_hls(r, g, b)
    s = amount
    r, g, b = hls_to_rgb(h, l, s)
    r, g, b = [x * 255.0 for x in (r, g, b)]

    return rgb_to_hex((int(r), int(g), int(b)))

def adjust(colors, light):
    """
    Adjust the generated colors in a list.
    """
    raw_colors = colors[:1] + colors[8:16] + colors[8:-1]

    # Manually adjust colors.
    if light:
        for color in raw_colors:
            color = saturate_color(color, 0.5)

        raw_colors[0] = lighten_color(colors[-1], 0.85)
        raw_colors[7] = colors[0]
        raw_colors[8] = darken_color(colors[-1], 0.4)
        raw_colors[15] = colors[0]

    else:
        # Darken the background color slightly.
        if raw_colors[0][1] != "0":
            raw_colors[0] = darken_color(raw_colors[0], 0.40)

        raw_colors[7] = blend_color(raw_colors[7], "#EEEEEE")
        raw_colors[8] = darken_color(raw_colors[7], 0.30)
        raw_colors[15] = blend_color(raw_colors[15], "#EEEEEE")

    return raw_colors


def save_as_json(user, theme, output_name, raw_colors):
    dictionary = {
        "main-bg": raw_colors[0],
        "main-fg": raw_colors[5],
        "wb-act-bg": raw_colors[1],
        "wb-act-fg": raw_colors[4],
        "wb-hvr-bg": raw_colors[2],
        "wb-hvr-fg": raw_colors[3]
    }
    if not os.path.exists(f"/home/{user}/.cache/color_schemes"):
        os.mkdir(f"/home/{user}/.cache/color_schemes")
    if not os.path.exists(f"/home/{user}/.cache/color_schemes/{theme}"):
        os.mkdir(f"/home/{user}/.cache/color_schemes/{theme}")
    with open(f"/home/{user}/.cache/color_schemes/{theme}/{output_name}.json", "w") as f:
        f.write(json.dumps(dictionary, indent=4))

def get_color_scheme(user, img, theme, output_name, light=False):
    """
    Get color_scheme.
    """
    colors = gen_colors(img)
    save_as_json(user, theme, output_name, adjust(colors, light))

def get_user():
    return sp.run("whoami", shell=True, capture_output=True, text=True).stdout.strip()

def get_images(user):
    """
    returns a list contains info about images:
    images_info : [
                    [ image path, name of theme, name of image]
                ]
    """
    themes = os.listdir(f"/home/{user}/.config/wallpapers")
    images_info = []
    for theme in themes:
        images = os.listdir(f"/home/{user}/.config/wallpapers/{theme}")
        for image in images:
            img = f"/home/{user}/.config/wallpapers/{theme}/{image}"
            images_info.append([img, theme, image.replace(".png", "").replace(".jpg", "").replace(".gif", "").replace(".jpeg", "")])
    return images_info

user = get_user()
images_info = get_images(user)

for image_info in images_info:
    print(image_info[0])
    if os.path.exists(f"/home/{user}/.cache/color_schemes/{image_info[1]}/{image_info[2]}.json"):
        print(f"exists:  /home/{user}/.cache/color_schemes/{image_info[1]}/{image_info[2]}.json")
    else:
        try:
            get_color_scheme(user, image_info[0], image_info[1], image_info[2])
        except Exception as e:
            with open(f"/home/{user}/.cache/color_schemes/{image_info[1]}/{image_info[2]}.error", "w") as f:
                f.writelines("Error:\n")
                f.writelines(f"{e}:\n")
                f.writelines(f"{image_info[0]}\n")
                f.writelines(f"{image_info[1]}\n")
                f.writelines(f"{image_info[2]}\n")