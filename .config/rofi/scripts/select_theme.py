import subprocess as sp
import time
import json

#%% Themes
themes = {
    "Catppuccin-Latte": {
        "icon-theme": "Tela-circle-grey",
        "color-scheme": "prefer-light",
        "cursor-theme": "Bibata-Modern-Classic"
    },
    "Catppuccin-Mocha": {
        "icon-theme": "Tela-circle-dracula",
        "color-scheme": "prefer-dark",
        "cursor-theme": "Bibata-Modern-Classic"
    },
    "Cyberpunk-Edge": {
        "icon-theme": "Tela-circle-yellow",
        "color-scheme": "prefer-dark",
        "cursor-theme": "Bibata-Modern-Classic"
    },
    "Decay-Green": {
        "icon-theme": "Tela-circle-green",
        "color-scheme": "prefer-dark",
        "cursor-theme": "Bibata-Modern-Classic"
    },
    "Dracula": {
        "icon-theme": "Tela-circle-dracula",
        "color-scheme": "prefer-dark",
        "cursor-theme": "Dracula-cursors"
    },
    "Frosted-Glass": {
        "icon-theme": "Tela-circle-blue",
        "color-scheme": "prefer-light",
        "cursor-theme": "Bibata-Modern-Classic"
    },
    "Graphite-Mono": {
        "icon-theme": "Tela-circle-grey",
        "color-scheme": "prefer-dark",
        "cursor-theme": "Bibata-Modern-Classic"
    },
    "Gruvbox": {
        "icon-theme": "Gruvbox-Plus-Dark",
        "color-scheme": "prefer-dark",
        "cursor-theme": "Gruvbox-Retro"
    },
    "Gruvbox-Retro": {
        "icon-theme": "Gruvbox-Plus-Dark",
        "color-scheme": "prefer-dark",
        "cursor-theme": "Gruvbox-Retro"
    },
    "Material-Sakura": {
        "icon-theme": "Tela-circle-grey",
        "color-scheme": "prefer-light",
        "cursor-theme": "Bibata-Modern-Classic"
    },
    "Nordic-Blue": {
        "icon-theme": "Nordzy",
        "color-scheme": "prefer-dark",
        "cursor-theme": "Bibata-Modern-Classic"
    },
    "Rose-Pine": {
        "icon-theme": "Tela-circle-pink",
        "color-scheme": "prefer-dark",
        "cursor-theme": "Bibata-Modern-Classic"
    },
    "Sweet-Mars": {
        "icon-theme": "candy-icons",
        "color-scheme": "prefer-dark",
        "cursor-theme": "Sweet-cursors"
    },
    "Synth-Wave": {
        "icon-theme": "BeautyLine",
        "color-scheme": "prefer-dark",
        "cursor-theme": "Bibata-Modern-Classic"
    },
    "Tokyo-Night": {
        "icon-theme": "Tela-circle-purple",
        "color-scheme": "prefer-dark",
        "cursor-theme": "Bibata-Modern-Classic"
    },
}

#%% Rofi
# Create available theme options string for rofi
rofi_output = ""
for theme in list(themes.keys()):
    if rofi_output == "":
        rofi_output = f"""{theme}"""
    else:
        rofi_output = f"""{rofi_output}\n{theme}"""

# Send created string to rofi and get selected rofi output
rofi_select = sp.run(f"""echo "{rofi_output}" | rofi -dmenu -matching normal -i""", shell=True, capture_output=True, text=True,)
rofi_selected = rofi_select.stdout.strip()

icon_theme = themes[rofi_selected]["icon-theme"]
gtk_theme = rofi_selected
color_scheme = themes[rofi_selected]["color-scheme"]
cursor_theme = themes[rofi_selected]["cursor-theme"]
qt_theme = rofi_selected
hypr_theme = rofi_selected
rofi_theme = rofi_selected
kitty_theme = rofi_selected
waybar_theme = rofi_selected
dunst_theme = rofi_selected
wlogout_theme = rofi_selected
btop_theme = rofi_selected
starship_theme = rofi_selected
vscodium_theme = rofi_selected
nvim_theme = rofi_selected

#%% User
user = sp.run("whoami", shell=True, capture_output=True, text=True,).stdout.strip()

#%% Hyprland
# Update conf
with open(f"/home/{user}/.config/hypr/themes/theme.conf", "w", encoding="UTF-8") as file:
    file.write(f"""source = ~/.config/hypr/themes/{hypr_theme}.conf """)

# Update hyprctl
sp.run(f"""hyprctl setcursor {cursor_theme} 24""", shell=True,)
sp.run("""hyprctl reload""", shell=True,)
print("Hyprland hyprctl Completed")

#%% Save for startup
with open(f"/home/{user}/.config/hypr/confs/last_selected_theme.conf", "w", encoding="UTF-8") as file:
    file.write(f"""exec-once = hyprctl setcursor {cursor_theme} 24\n""")
    file.write(f"""exec-once = gsettings set org.gnome.desktop.interface cursor-theme '{cursor_theme}'\n""")
    file.write("""exec-once = gsettings set org.gnome.desktop.interface cursor-size 24\n""")
    file.write(f"""exec-once = gsettings set org.gnome.desktop.interface icon-theme '{icon_theme}'\n""")
    file.write(f"""exec-once = gsettings set org.gnome.desktop.interface gtk-theme '{gtk_theme}'\n""")
    file.write(f"""exec-once = gsettings set org.gnome.desktop.interface color-scheme '{color_scheme}'\n""")
print("Hyprland Save for startup Completed")

#%% Kvantum (Qt5/Qt6)
# Kvantum
with open(f"/home/{user}/.config/Kvantum/kvantum.kvconfig", "w", encoding="UTF-8",) as f:
    f.write(f"""[General]\ntheme={qt_theme}""")
print("Hyprland Kvantum Completed")

# Recreate qt5ct.conf file for colors
with open(f"/home/{user}/.config/qt5ct/qt5ct.conf", "r", encoding="UTF-8") as file:
    data = file.readlines()
# replace specific lines
data[1] = f"color_scheme_path=~/.config/qt5ct/colors/{qt_theme}.conf\n"
data[3] = f"icon_theme={icon_theme}\n"

with open(f"/home/{user}/.config/qt5ct/qt5ct.conf", "w", encoding="UTF-8") as file:
    file.writelines(data)
print("qt5ct Completed")

# Recreate qt6ct.conf file for colors
with open(f"/home/{user}/.config/qt6ct/qt6ct.conf", "r", encoding="UTF-8") as file:
    data = file.readlines()
# replace specific lines
data[1] = f"color_scheme_path=~/.config/qt6ct/colors/{qt_theme}.conf\n"
data[3] = f"icon_theme={icon_theme}\n"

with open(f"/home/{user}/.config/qt6ct/qt6ct.conf", "w", encoding="UTF-8") as file:
    file.writelines(data)
print("qt6ct Completed")

#%% GTK Theme/Icon
# gsetings
sp.run(f"""gsettings set org.gnome.desktop.interface cursor-theme '{cursor_theme}'""", shell=True,)
sp.run("""gsettings set org.gnome.desktop.interface cursor-size 24""", shell=True,)
sp.run(f"""gsettings set org.gnome.desktop.interface icon-theme '{icon_theme}'""", shell=True,)
sp.run(f"""gsettings set org.gnome.desktop.interface gtk-theme '{gtk_theme}'""", shell=True,)
sp.run(f"""gsettings set org.gnome.desktop.interface color-scheme '{color_scheme}'""", shell=True,)
print("gsettings Completed")

# gtk-2.0
with open(f"/home/{user}/.gtkrc-2.0", "r", encoding="UTF-8") as file:
    data = file.readlines()
# replace specific lines
data[4] = f"""gtk-theme-name="{gtk_theme}"\n"""
data[5] = f"""gtk-icon-theme-name="{icon_theme}"\n"""
data[7] = f"""gtk-cursor-theme-name="{cursor_theme}"\n"""

with open(f"/home/{user}/.gtkrc-2.0", "w", encoding="UTF-8") as file:
    file.writelines(data)
print("gtk-2.0 Completed")

# gtk-3.0
with open(f"/home/{user}/.config/gtk-3.0/settings.ini", "r", encoding="UTF-8") as file:
    data = file.readlines()
# replace specific lines
data[1] = f"gtk-theme-name={gtk_theme}\n"
data[2] = f"gtk-icon-theme-name={icon_theme}\n"
data[4] = f"gtk-cursor-theme-name={cursor_theme}\n"

with open(f"/home/{user}/.config/gtk-3.0/settings.ini", "w", encoding="UTF-8") as file:
    file.writelines(data)
print("gtk-3.0 Completed")

# .icons/default
with open(f"/home/{user}/.icons/default/index.theme", "r", encoding="UTF-8") as file:
    data = file.readlines()
# replace specific lines
# data[3] = f"Comment={cursor_theme}\n"
data[4] = f"Inherits={cursor_theme}\n"

with open(f"/home/{user}/.icons/default/index.theme", "w", encoding="UTF-8") as file:
    file.writelines(data)
print(".icons/default Completed")

print("GTK Theme/Icon Completed")

#%% Rofi Theme
with open(f"/home/{user}/.config/rofi/themes/theme.rasi", "w", encoding="UTF-8") as file:
    file.write(f'''@theme "~/.config/rofi/themes/{rofi_theme}.rasi"''')
print("Rofi Theme Completed")

#%% Kitty Theme
with open(f"/home/{user}/.config/kitty/themes/theme.conf", "w", encoding="UTF-8") as file:
    file.write(f"""include /home/{user}/.config/kitty/themes/{kitty_theme}.conf""")
print("Kitty Theme Completed")

#%% Waybar
# Change Theme
with open(f"/home/{user}/.config/waybar/themes/theme.css", "w", encoding="UTF-8") as file:
    file.write(f'''@import "{waybar_theme}.css";''')

# Reset Waybar
sp.run("killall waybar", shell=True)
time.sleep(1)
sp.run("waybar &", shell=True)
print("Waybar Completed")

#%% Dunst
# Update dunst config
with open(f"/home/{user}/.config/dunst/themes/{dunst_theme}.json", "r") as file:
    dunst_json = json.load(file)

with open(f"/home/{user}/.config/dunst/dunstrc", "r", encoding="UTF-8") as file:
    data = file.readlines()

# [urgency_low]
data[294] = f"""    background = "{dunst_json["main-bg"]}"\n"""
data[295] = f"""    foreground = "{dunst_json["main-fg"]}"\n"""
data[296] = f"""    frame_color = "{dunst_json["wb-hvr-bg"]}"\n"""

# [urgency_normal]
data[301] = f"""    background = "{dunst_json["main-bg"]}"\n"""
data[302] = f"""    foreground = "{dunst_json["main-fg"]}"\n"""
data[303] = f"""    frame_color = "{dunst_json["wb-hvr-bg"]}"\n"""

with open(f"/home/{user}/.config/dunst/dunstrc", "w", encoding="UTF-8") as file:
    file.writelines(data)

# Update vol svg to ~/.cache/dunst/icons/vol
for vol in range(0, 101, 5):
    with open(f"/home/{user}/.config/dunst/icons/vol/vol-{vol}.svg", "r", encoding="UTF-8") as file:
        data = file.readlines()

    data[51] = f"""fill:{dunst_json["wb-hvr-fg"]};\n""" # background color
    data[91] = f"""fill:{dunst_json["wb-hvr-bg"]};\n""" # indicator color
    
    with open(f"/home/{user}/.config/dunst/icons/vol/vol-{vol}.svg", "w", encoding="UTF-8") as file:
        file.writelines(data)

# Update vol svg to ~/.cache/dunst/icons/status
# mic
for status in ["mic-muted", "mic-unmuted"]:
    with open(f"/home/{user}/.config/dunst/icons/status/{status}.svg", "r", encoding="UTF-8") as file:
        data = file.readlines()

    data[7] = f"""stroke="{dunst_json["wb-hvr-bg"]}"\n""" # indicator color
    
    with open(f"/home/{user}/.config/dunst/icons/status/{status}.svg", "w", encoding="UTF-8") as file:
        file.writelines(data)

# speaker
for status in ["speaker-muted", "speaker-unmuted"]:
    with open(f"/home/{user}/.config/dunst/icons/status/{status}.svg", "r", encoding="UTF-8") as file:
        data = file.readlines()

    data[2] = f"""fill="{dunst_json["wb-hvr-bg"]}"\n""" # indicator color
    
    with open(f"/home/{user}/.config/dunst/icons/status/{status}.svg", "w", encoding="UTF-8") as file:
        file.writelines(data)

# lock
for status in ["lock-locked", "lock-unlocked"]:
    with open(f"/home/{user}/.config/dunst/icons/status/{status}.svg", "r", encoding="UTF-8") as file:
        data = file.readlines()

    data[3] = f"""stroke="{dunst_json["wb-hvr-bg"]}"\n""" # indicator color
    
    with open(f"/home/{user}/.config/dunst/icons/status/{status}.svg", "w", encoding="UTF-8") as file:
        file.writelines(data)

# Reset dunst
sp.run("killall dunst", shell=True)
time.sleep(1)
sp.run("dunst &", shell=True)
print("Dunst Completed")

#%% Wlogout
with open(f"/home/{user}/.config/wlogout/themes/theme.css", "w", encoding="UTF-8") as file:
    file.write(f'''@import "{wlogout_theme}.css";''')
print("Wlogout Completed")

#%% Btop
# Recreate btop.conf file for colors
with open(f"/home/{user}/.config/btop/btop.conf", "r", encoding="UTF-8") as file:
    data = file.readlines()
# replace specific lines
data[4] = f"""color_theme = "/home/spidy/.config/btop/themes/{btop_theme}.theme"\n"""

with open(f"/home/{user}/.config/btop/btop.conf", "w", encoding="UTF-8") as file:
    file.writelines(data)
print("Btop Completed")

#%% Starship Theme

#%% Neovim Theme

#%% VSCodium

#%% Waypaper
# Recreate config.ini file for colors
with open(f"/home/{user}/.config/waypaper/config.ini", "r", encoding="UTF-8") as file:
    data = file.readlines()
# replace specific lines
data[2] = f"""folder = /home/{user}/.config/wallpapers/{rofi_selected}\n"""

with open(f"/home/{user}/.config/waypaper/config.ini", "w", encoding="UTF-8") as file:
    file.writelines(data)
print("Btop Completed")
