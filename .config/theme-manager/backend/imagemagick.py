import subprocess as sp

def imagemagick(img):
    """Call Imagemagick to generate a scheme."""
    color_palette = sp.run(f"""magick {img} -resize 25% -colors 8 -unique-colors txt:-""", shell=True, capture_output=True, text=True).stdout.splitlines()
    if len(color_palette)>=8:
        print("unique-colors")
        color_palette = [i.split(" ")[2] for i in color_palette[1:]]
        return color_palette
    print("kmeans")
    color_palette = sp.run(f"""magick {img} -depth 8 -fuzz 70% +dither -kmeans 8 -depth 8 -format "%c" histogram:info:""", shell=True, capture_output=True, text=True).stdout.strip()
    return color_palette

# img = "/home/spidy/.config/wallpapers/Material-Red/god_of_war_omega.jpg"
img = "/home/spidy/.config/wallpapers/Material-Red/spider_man_symbol.jpg"
# img = "/home/spidy/.config/wallpapers/Catppuccin-Mocha/fantasy_landscape.png"
print(img)
data = imagemagick(img)
print(data)
