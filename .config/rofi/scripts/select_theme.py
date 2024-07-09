#!/usr/bin/python
import subprocess as sp
import time
import json

user = sp.run("whoami", shell=True, capture_output=True, text=True,).stdout.strip()

def get_config():
    """
    Get main config file from ~/.config/themes_config.json
    """

    with open(f"/home/{user}/.config/themes_config.json", "r") as f:
        config = json.load(f)
    return config

def rofi_select_theme(config):
    """
    Create available theme options string for rofi

    config: Config file that includes theming infos
    """
    rofi_output = ""
    for theme in list(config.keys()):
        if rofi_output == "":
            rofi_output = f"""{theme}"""
        else:
            rofi_output = f"""{rofi_output}\n{theme}"""

    # Send created string to rofi and get selected rofi output
    rofi_select = sp.run(f"""echo "{rofi_output}" | rofi -dmenu -matching normal -i""", shell=True, capture_output=True, text=True,)
    rofi_selected = rofi_select.stdout.strip()
    config_theme = config[rofi_selected]

    return config_theme, rofi_selected

def hyprland(hypr_theme, gtk_theme, cursor_theme, icon_theme, color_scheme):
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

def kvantum(theme):
    """
    This function creates/overwrites ~/.config/Kvantum/kvantum.kvconfig file.
    
    theme: Name of the theme. Ex. Catppuccin-Mocha
    """
    
    # Kvantum
    with open(f"/home/{user}/.config/Kvantum/kvantum.kvconfig", "w", encoding="UTF-8",) as f:
        f.write(f"""[General]\ntheme={theme}""")
    print("Hyprland Kvantum Completed")

def qt5ct(theme, icon_theme, theme_line=1, icon_theme_line=3):
    """
    This function overwrites ~/.config/qt5ct/qt5ct.conf file.
    
    theme: Name of the theme. Ex. Catppuccin-Mocha
    icon_theme: Name of the icon theme. Ex. Tela-circle-dracula
    theme_line: Line index of the 'color_scheme_path=' parameter
    icon_theme_line: Line index of the 'icon_theme=' parameter
    """

    # Recreate qt5ct.conf file for colors
    with open(f"/home/{user}/.config/qt5ct/qt5ct.conf", "r", encoding="UTF-8") as file:
        data = file.readlines()
    # replace specific lines
    data[theme_line] = f"color_scheme_path=~/.config/qt5ct/colors/{theme}.conf\n"
    data[icon_theme_line] = f"icon_theme={icon_theme}\n"

    with open(f"/home/{user}/.config/qt5ct/qt5ct.conf", "w", encoding="UTF-8") as file:
        file.writelines(data)
    print("qt5ct Completed")

def qt6ct(theme, icon_theme, theme_line=1, icon_theme_line=3):
    """
    This function overwrites ~/.config/qt6ct/qt6ct.conf file.
    
    theme: Name of the theme. Ex. Catppuccin-Mocha
    icon_theme: Name of the icon theme. Ex. Tela-circle-dracula
    theme_line: Line index of the 'color_scheme_path=' parameter
    icon_theme_line: Line index of the 'icon_theme=' parameter
    """

    # Recreate qt6ct.conf file for colors
    with open(f"/home/{user}/.config/qt6ct/qt6ct.conf", "r", encoding="UTF-8") as file:
        data = file.readlines()
    # replace specific lines
    data[theme_line] = f"color_scheme_path=~/.config/qt6ct/colors/{theme}.conf\n"
    data[icon_theme_line] = f"icon_theme={icon_theme}\n"

    with open(f"/home/{user}/.config/qt6ct/qt6ct.conf", "w", encoding="UTF-8") as file:
        file.writelines(data)
    print("qt6ct Completed")

def gsettings(theme, icon_theme, cursor_theme, color_scheme):
    """
    This function runs gsettings for selected theme

    theme: Name of the theme. Ex. Catppuccin-Mocha
    icon_theme: Name of the icon theme. Ex. Tela-circle-dracula
    cursor_theme: Name of the cursor theme. Ex. Bibata-Modern-Classic
    color_scheme: Name of the color theme. Ex. prefer-dark
    """

    # gsetings
    sp.run(f"""gsettings set org.gnome.desktop.interface cursor-theme '{cursor_theme}'""", shell=True,)
    sp.run("""gsettings set org.gnome.desktop.interface cursor-size 24""", shell=True,)
    sp.run(f"""gsettings set org.gnome.desktop.interface icon-theme '{icon_theme}'""", shell=True,)
    sp.run(f"""gsettings set org.gnome.desktop.interface gtk-theme '{theme}'""", shell=True,)
    sp.run(f"""gsettings set org.gnome.desktop.interface color-scheme '{color_scheme}'""", shell=True,)
    print("gsettings Completed")

def gtk_2(theme, icon_theme, cursor_theme, theme_line=4, icon_theme_line=5, cursor_theme_line=7):
    """
    This function overwrites ~/.gtkrc-2.0 file.

    theme: Name of the theme. Ex. Catppuccin-Mocha
    icon_theme: Name of the icon theme. Ex. Tela-circle-dracula
    cursor_theme: Name of the cursor theme. Ex. Bibata-Modern-Classic
    theme_line: Line index of the 'gtk-theme-name=' parameter
    icon_theme_line: Line index of the 'gtk-icon-theme-name=' parameter
    cursor_theme_line: Line index of the 'gtk-cursor-theme-name=' parameter
    """

    # gtk-2.0
    with open(f"/home/{user}/.gtkrc-2.0", "r", encoding="UTF-8") as file:
        data = file.readlines()
    # replace specific lines
    data[theme_line] = f"""gtk-theme-name="{theme}"\n"""
    data[icon_theme_line] = f"""gtk-icon-theme-name="{icon_theme}"\n"""
    data[cursor_theme_line] = f"""gtk-cursor-theme-name="{cursor_theme}"\n"""

    with open(f"/home/{user}/.gtkrc-2.0", "w", encoding="UTF-8") as file:
        file.writelines(data)
    print("gtk-2.0 Completed")

def gtk_3(theme, icon_theme, cursor_theme, theme_line=1, icon_theme_line=2, cursor_theme_line=4):
    # gtk-3.0
    with open(f"/home/{user}/.config/gtk-3.0/settings.ini", "r", encoding="UTF-8") as file:
        data = file.readlines()
    # replace specific lines
    data[theme_line] = f"gtk-theme-name={theme}\n"
    data[icon_theme_line] = f"gtk-icon-theme-name={icon_theme}\n"
    data[cursor_theme_line] = f"gtk-cursor-theme-name={cursor_theme}\n"

    with open(f"/home/{user}/.config/gtk-3.0/settings.ini", "w", encoding="UTF-8") as file:
        file.writelines(data)
    print("gtk-3.0 Completed")

def icons_default(cursor_theme, cursor_theme_line=4):
    """
    This function overwrites ~/.icons/default/index.theme file.

    cursor_theme: Name of the cursor theme. Ex. Bibata-Modern-Classic
    cursor_theme_line: Line index of the 'Inherits=' parameter
    """

    # .icons/default
    with open(f"/home/{user}/.icons/default/index.theme", "r", encoding="UTF-8") as file:
        data = file.readlines()
    # replace specific lines
    # data[3] = f"Comment={cursor_theme}\n"
    data[cursor_theme_line] = f"Inherits={cursor_theme}\n"

    with open(f"/home/{user}/.icons/default/index.theme", "w", encoding="UTF-8") as file:
        file.writelines(data)
    print(".icons/default Completed")

def rofi(theme):
    """
    This function creates/overwrites ~/.config/rofi/themes/theme.rasi file.

    theme: Name of the theme. Ex. Catppuccin-Mocha
    """

    with open(f"/home/{user}/.config/rofi/themes/theme.rasi", "w", encoding="UTF-8") as file:
        file.write(f'''@theme "~/.config/rofi/themes/{theme}.rasi"''')
    print("Rofi Theme Completed")

def kitty(theme):
    """
    This function creates/overwrites ~/.config/kitty/themes/theme.conf file.

    theme: Name of the theme. Ex. Catppuccin-Mocha
    """

    with open(f"/home/{user}/.config/kitty/themes/theme.conf", "w", encoding="UTF-8") as file:
        file.write(f"""include /home/{user}/.config/kitty/themes/{theme}.conf""")
    print("Kitty Theme Completed")

def waybar(theme):
    """
    This function creates/overwrites ~/.config/waybar/themes/theme.css file.

    theme: Name of the theme. Ex. Catppuccin-Mocha
    """

    # Change Theme
    with open(f"/home/{user}/.config/waybar/themes/theme.css", "w", encoding="UTF-8") as file:
        file.write(f'''@import "{theme}.css";''')

    # Reset Waybar
    sp.run("killall waybar", shell=True)
    time.sleep(1)
    sp.run("waybar &", shell=True)
    print("Waybar Completed")

def notification_icons(theme, vol_line1=51, vol_line2=91, mic_line=7, speaker_line=2, lock_line=3):
    """
    This function overwrites these icons:
        .config/dunst/icons/vol/vol-*.svg
        .config/dunst/icons/status/mic-*.svg
        .config/dunst/icons/status/speaker-*.svg
        .config/dunst/icons/status/lock-*.svg

    theme: Name of the theme. Ex. Catppuccin-Mocha
    vol_line1: Line index of the 'fill:' parameter for background color
    vol_line2: Line index of the 'fill:' parameter for indicator color
    mic_line: Line index of the 'stroke=' parameter for indicator color
    speaker_line: Line index of the 'fill:' parameter for indicator color
    lock_line: Line index of the 'stroke=' parameter for indicator color
    """

    # Get colors for icons
    with open(f"/home/{user}/.config/dunst/themes/{theme}.json", "r") as file:
        dunst_json = json.load(file)

    # Update vol svg to ~/.cache/dunst/icons/vol
    for vol in range(0, 101, 5):
        with open(f"/home/{user}/.config/dunst/icons/vol/vol-{vol}.svg", "r", encoding="UTF-8") as file:
            data = file.readlines()

        data[vol_line1] = f"""fill:{dunst_json["wb-hvr-fg"]};\n""" # background color
        data[vol_line2] = f"""fill:{dunst_json["wb-hvr-bg"]};\n""" # indicator color
        
        with open(f"/home/{user}/.config/dunst/icons/vol/vol-{vol}.svg", "w", encoding="UTF-8") as file:
            file.writelines(data)

    # Update vol svg to ~/.cache/dunst/icons/status
    # mic
    for status in ["mic-muted", "mic-unmuted"]:
        with open(f"/home/{user}/.config/dunst/icons/status/{status}.svg", "r", encoding="UTF-8") as file:
            data = file.readlines()

        data[mic_line] = f"""stroke="{dunst_json["wb-hvr-bg"]}"\n""" # indicator color
        
        with open(f"/home/{user}/.config/dunst/icons/status/{status}.svg", "w", encoding="UTF-8") as file:
            file.writelines(data)

    # speaker
    for status in ["speaker-muted", "speaker-unmuted"]:
        with open(f"/home/{user}/.config/dunst/icons/status/{status}.svg", "r", encoding="UTF-8") as file:
            data = file.readlines()

        data[speaker_line] = f"""fill="{dunst_json["wb-hvr-bg"]}"\n""" # indicator color
        
        with open(f"/home/{user}/.config/dunst/icons/status/{status}.svg", "w", encoding="UTF-8") as file:
            file.writelines(data)

    # lock
    for status in ["lock-locked", "lock-unlocked"]:
        with open(f"/home/{user}/.config/dunst/icons/status/{status}.svg", "r", encoding="UTF-8") as file:
            data = file.readlines()

        data[lock_line] = f"""stroke="{dunst_json["wb-hvr-bg"]}"\n""" # indicator color
        
        with open(f"/home/{user}/.config/dunst/icons/status/{status}.svg", "w", encoding="UTF-8") as file:
            file.writelines(data)
    print("Notification Icons Updated")

def dunst(theme, ulow_bckgrnd_line=294, ulow_frgrnd_line=295, ulow_fr_color_line=296,
                    un_bckgrnd_line=301, un_frgrnd_line=302, un_fr_color_line=303):
    """
    This function overwrites ~/.config/waybar/themes/theme.css file and resets dunst.

    theme: Name of the theme. Ex. Catppuccin-Mocha
    """

    # Get colors for dunstrc
    with open(f"/home/{user}/.config/dunst/themes/{theme}.json", "r") as file:
        dunst_json = json.load(file)

    # Update dunst config
    with open(f"/home/{user}/.config/dunst/dunstrc", "r", encoding="UTF-8") as file:
        data = file.readlines()

    # [urgency_low]
    data[ulow_bckgrnd_line] = f"""    background = "{dunst_json["main-bg"]}"\n"""
    data[ulow_frgrnd_line] = f"""    foreground = "{dunst_json["main-fg"]}"\n"""
    data[ulow_fr_color_line] = f"""    frame_color = "{dunst_json["wb-hvr-bg"]}"\n"""

    # [urgency_normal]
    data[un_bckgrnd_line] = f"""    background = "{dunst_json["main-bg"]}"\n"""
    data[un_frgrnd_line] = f"""    foreground = "{dunst_json["main-fg"]}"\n"""
    data[un_fr_color_line] = f"""    frame_color = "{dunst_json["wb-hvr-bg"]}"\n"""

    with open(f"/home/{user}/.config/dunst/dunstrc", "w", encoding="UTF-8") as file:
        file.writelines(data)
    
    # Reset dunst
    sp.run("killall dunst", shell=True)
    time.sleep(1)
    sp.run("dunst &", shell=True)
    print("Dunst Completed")

def wlogout(theme):
    """
    This function creates/overwrites ~/.config/wlogout/themes/theme.css file.

    theme: Name of the theme. Ex. Catppuccin-Mocha
    """

    with open(f"/home/{user}/.config/wlogout/themes/theme.css", "w", encoding="UTF-8") as file:
        file.write(f'''@import "{theme}.css";''')
    print("Wlogout Completed")
    
def btop(theme, theme_line=4):
    """
    This function overwrites ~/.config/btop/btop.conf file.

    theme: Name of the theme. Ex. Catppuccin-Mocha
    theme_line: Line index of the 'color_theme = ' parameter
    """

    # Recreate btop.conf file for colors
    with open(f"/home/{user}/.config/btop/btop.conf", "r", encoding="UTF-8") as file:
        data = file.readlines()
    # replace specific lines
    data[theme_line] = f"""color_theme = "/home/spidy/.config/btop/themes/{theme}.theme"\n"""

    with open(f"/home/{user}/.config/btop/btop.conf", "w", encoding="UTF-8") as file:
        file.writelines(data)
    print("Btop Completed")

def waypaper(theme, theme_line=2):
    """
    This function overwrites ~/.config/waypaper/config.ini file.

    theme: Name of the theme. Ex. Catppuccin-Mocha
    theme_line: Line index of the 'folder = ' parameter
    """

    # Recreate config.ini file for colors
    with open(f"/home/{user}/.config/waypaper/config.ini", "r", encoding="UTF-8") as file:
        data = file.readlines()
    # replace specific lines
    data[theme_line] = f"""folder = /home/{user}/.config/wallpapers/{theme}\n"""

    with open(f"/home/{user}/.config/waypaper/config.ini", "w", encoding="UTF-8") as file:
        file.writelines(data)
    print("Btop Completed")

def main():
    
    config = get_config()
    config_theme, theme = rofi_select_theme(config)
    
    hyprland(hypr_theme=theme, gtk_theme=theme, cursor_theme=config_theme["cursor-theme"], icon_theme=config_theme["icon-theme"], color_scheme=config_theme["color-scheme"])
    
    kvantum(theme)
    qt5ct(theme, icon_theme=config_theme["icon-theme"], theme_line=1, icon_theme_line=3)
    qt6ct(theme, icon_theme=config_theme["icon-theme"], theme_line=1, icon_theme_line=3)
    print("QT Theming Completed")

    gsettings(theme, icon_theme=config_theme["icon-theme"], cursor_theme=config_theme["cursor-theme"], color_scheme=config_theme["color-scheme"])
    gtk_2(theme, icon_theme=config_theme["icon-theme"], cursor_theme=config_theme["cursor-theme"], theme_line=4, icon_theme_line=5, cursor_theme_line=7)
    gtk_3(theme, icon_theme=config_theme["icon-theme"], cursor_theme=config_theme["cursor-theme"], theme_line=1, icon_theme_line=2, cursor_theme_line=4)
    icons_default(cursor_theme=config_theme["cursor-theme"], cursor_theme_line=4)
    print("GTK Theming Completed")

    rofi(theme)
    kitty(theme)
    btop(theme, theme_line=4)
    waybar(theme)
    wlogout(theme)
    waypaper(theme, theme_line=2)
    
    notification_icons(theme, vol_line1=51, vol_line2=91, mic_line=7, speaker_line=2, lock_line=3)
    dunst(theme, ulow_bckgrnd_line=294, ulow_frgrnd_line=295, ulow_fr_color_line=296,
                    un_bckgrnd_line=301, un_frgrnd_line=302, un_fr_color_line=303)

    # Starship Theme
    # Neovim Theme
    # VSCodium


if __name__ == "__main__":
    main()
