from colorthief import ColorThief

color_thief = ColorThief("/home/spidy/.config/wallpapers/Material-Red/god_of_war_omega.jpg")
# get the dominant color
dominant_color = color_thief.get_color(quality=1)
# build a color palette
palette = color_thief.get_palette(color_count=11)
print(len(palette))
print(palette)
for rgb_color in palette:
    hex_color = color_thief.rgb_to_hex(rgb_color)
    print(hex_color)