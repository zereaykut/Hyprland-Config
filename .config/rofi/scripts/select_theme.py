#!/usr/bin/python
import os
import subprocess as sp
import time
import json

class ThemeManager:
    def __init__(self):
        self.user = sp.run("whoami", shell=True, capture_output=True, text=True).stdout.strip()
        self.config = self.get_config()

    def get_config(self):
        with open(f"/home/{self.user}/.config/themes_config.json", "r") as f:
            return json.load(f)

    def rofi_select_theme(self):
        rofi_output = "\n".join(self.config.keys())
        rofi_select = sp.run(f"""echo "{rofi_output}" | rofi -dmenu -matching normal -i""", shell=True, capture_output=True, text=True)
        rofi_selected = rofi_select.stdout.strip()
        return self.config[rofi_selected], rofi_selected

    def rofi_select_wallpaper(self, theme):
        wallpapers = os.listdir(f"""/home/{self.user}/.config/wallpapers/{theme}""")
        rofi_output = "\n".join(wallpapers)
        rofi_select = sp.run(f"""echo "{rofi_output}" | rofi -dmenu -matching normal -i""", shell=True, capture_output=True, text=True)
        wallpaper = rofi_select.stdout.strip()
        color_scheme = wallpaper.replace(".png", "").replace(".jpg", "")
        with open(f"/home/{self.user}/.cache/color_schemes/{theme}/{color_scheme}.json", "r") as f:
            color_config = json.load(f)
        return f"/home/{self.user}/.config/wallpapers/{theme}/{wallpaper}", color_config

    def get_random_wall_and_col(self, theme):
        wallpapers = os.listdir(f"/home/{self.user}/.config/wallpapers/{theme}")
        rand_index = random.randint(0, len(wallpapers) - 1)
        wallpaper = wallpapers[rand_index]
        color_scheme = wallpaper.replace(".png", "").replace(".jpg", "")
        with open(f"/home/{self.user}/.cache/color_schemes/{theme}/{color_scheme}.json", "r") as f:
            color_config = json.load(f)
        return f"/home/{self.user}/.config/wallpapers/{theme}/{wallpaper}", color_config

    def change_wallpaper(self, wallpaper):
        sp.run(["swww img " + wallpaper, "--transition-type", "center"], shell=True)

    def update_hyprland(self, hypr_theme, gtk_theme, cursor_theme, icon_theme, color_scheme):
        with open(f"/home/{self.user}/.config/hypr/themes/theme.conf", "w", encoding="UTF-8") as file:
            file.write(f"""source = ~/.config/hypr/themes/{hypr_theme}.conf """)

        sp.run(f"""hyprctl setcursor {cursor_theme} 24""", shell=True)
        sp.run("""hyprctl reload""", shell=True)

        with open(f"/home/{self.user}/.config/hypr/confs/last_selected_theme.conf", "w", encoding="UTF-8") as file:
            file.write(f"""exec-once = hyprctl setcursor {cursor_theme} 24\n""")
            file.write(f"""exec-once = gsettings set org.gnome.desktop.interface cursor-theme '{cursor_theme}'\n""")
            file.write("""exec-once = gsettings set org.gnome.desktop.interface cursor-size 24\n""")
            file.write(f"""exec-once = gsettings set org.gnome.desktop.interface icon-theme '{icon_theme}'\n""")
            file.write(f"""exec-once = gsettings set org.gnome.desktop.interface gtk-theme '{gtk_theme}'\n""")
            file.write(f"""exec-once = gsettings set org.gnome.desktop.interface color-scheme '{color_scheme}'\n""")

    def update_kvantum(self, theme):
        with open(f"/home/{self.user}/.config/Kvantum/kvantum.kvconfig", "w", encoding="UTF-8") as f:
            f.write(f"""[General]\ntheme={theme}""")

    def update_qt5ct(self, theme, icon_theme, theme_line=1, icon_theme_line=3):
        with open(f"/home/{self.user}/.config/qt5ct/qt5ct.conf", "r", encoding="UTF-8") as file:
            data = file.readlines()
        data[theme_line] = f"color_scheme_path=~/.config/qt5ct/colors/{theme}.conf\n"
        data[icon_theme_line] = f"icon_theme={icon_theme}\n"
        with open(f"/home/{self.user}/.config/qt5ct/qt5ct.conf", "w", encoding="UTF-8") as file:
            file.writelines(data)

    def update_qt6ct(self, theme, icon_theme, theme_line=1, icon_theme_line=3):
        with open(f"/home/{self.user}/.config/qt6ct/qt6ct.conf", "r", encoding="UTF-8") as file:
            data = file.readlines()
        data[theme_line] = f"color_scheme_path=~/.config/qt6ct/colors/{theme}.conf\n"
        data[icon_theme_line] = f"icon_theme={icon_theme}\n"
        with open(f"/home/{self.user}/.config/qt6ct/qt6ct.conf", "w", encoding="UTF-8") as file:
            file.writelines(data)

    def update_gsettings(self, theme, icon_theme, cursor_theme, color_scheme):
        sp.run(f"""gsettings set org.gnome.desktop.interface cursor-theme '{cursor_theme}'""", shell=True)
        sp.run("""gsettings set org.gnome.desktop.interface cursor-size 24""", shell=True)
        sp.run(f"""gsettings set org.gnome.desktop.interface icon-theme '{icon_theme}'""", shell=True)
        sp.run(f"""gsettings set org.gnome.desktop.interface gtk-theme '{theme}'""", shell=True)
        sp.run(f"""gsettings set org.gnome.desktop.interface color-scheme '{color_scheme}'""", shell=True)

    def update_gtk_2(self, theme, icon_theme, cursor_theme, theme_line=4, icon_theme_line=5, cursor_theme_line=7):
        with open(f"/home/{self.user}/.gtkrc-2.0", "r", encoding="UTF-8") as file:
            data = file.readlines()
        data[theme_line] = f"""gtk-theme-name="{theme}"\n"""
        data[icon_theme_line] = f"""gtk-icon-theme-name="{icon_theme}"\n"""
        data[cursor_theme_line] = f"""gtk-cursor-theme-name="{cursor_theme}"\n"""
        with open(f"/home/{self.user}/.gtkrc-2.0", "w", encoding="UTF-8") as file:
            file.writelines(data)

    def update_gtk_3(self, theme, icon_theme, cursor_theme, theme_line=1, icon_theme_line=2, cursor_theme_line=4):
        with open(f"/home/{self.user}/.config/gtk-3.0/settings.ini", "r", encoding="UTF-8") as file:
            data = file.readlines()
        data[theme_line] = f"gtk-theme-name={theme}\n"
        data[icon_theme_line] = f"gtk-icon-theme-name={icon_theme}\n"
        data[cursor_theme_line] = f"gtk-cursor-theme-name={cursor_theme}\n"
        with open(f"/home/{self.user}/.config/gtk-3.0/settings.ini", "w", encoding="UTF-8") as file:
            file.writelines(data)

    def update_icons_default(self, cursor_theme, cursor_theme_line=4):
        with open(f"/home/{self.user}/.icons/default/index.theme", "r", encoding="UTF-8") as file:
            data = file.readlines()
        data[cursor_theme_line] = f"Inherits={cursor_theme}\n"
        with open(f"/home/{self.user}/.icons/default/index.theme", "w", encoding="UTF-8") as file:
            file.writelines(data)

    def update_rofi(self, color_config):
        with open(f"/home/{self.user}/.config/rofi/theme.rasi", "w", encoding="UTF-8") as file:
            file.writelines(["""* {\n""",
                            f"""main-bg:            {color_config["main-bg"]};\n""",
                            f"""main-fg:            {color_config["main-fg"]};\n""",
                            f"""main-br:            {color_config["wb-hvr-bg"]};\n""",
                            f"""main-ex:            {color_config["wb-act-bg"]};\n""",
                            f"""select-bg:          {color_config["wb-act-bg"]};\n""",
                            f"""select-fg:          {color_config["wb-hvr-fg"]};\n""",
                            """separatorcolor:     transparent;\n""",
                            """border-color:       transparent;\n""",
                            "}",])

    def update_kitty(self, theme):
        with open(f"/home/{self.user}/.config/kitty/themes/theme.conf", "w", encoding="UTF-8") as file:
            file.write(f"""include /home/{self.user}/.config/kitty/themes/{theme}.conf""")

    def update_waybar(self, color_config):
        with open(f"/home/{self.user}/.config/waybar/theme.css", "w", encoding="UTF-8") as file:
            file.writelines([f"""@define-color main-bg {color_config["main-bg"]};\n""",
                            f"""@define-color main-fg {color_config["main-fg"]};\n""",

                            f"""@define-color wb-act-bg {color_config["wb-act-bg"]};\n""",
                            f"""@define-color wb-act-fg {color_config["wb-act-fg"]};\n""",

                            f"""@define-color wb-hvr-bg {color_config["wb-hvr-bg"]};\n""",
                            f"""@define-color wb-hvr-fg {color_config["wb-hvr-fg"]};"""])
        sp.run({"killall waybar"}, shell=True)
        time.sleep(1)
        sp.run("waybar &", shell=True)

    def update_notification_icons(self, color_config, vol_line1=51, vol_line2=91, mic_line=7, speaker_line=2, lock_line=3):
        for vol in range(0, 101, 5):
            with open(f"/home/{self.user}/.config/dunst/icons/vol/vol-{vol}.svg", "r", encoding="UTF-8") as file:
                data = file.readlines()
            data[vol_line1] = f"""fill:{color_config["wb-hvr-fg"]};\n"""
            data[vol_line2] = f"""fill:{color_config["wb-hvr-bg"]};\n"""
            with open(f"/home/{self.user}/.config/dunst/icons/vol/vol-{vol}.svg", "w", encoding="UTF-8") as file:
                file.writelines(data)

        for status in ["mic-muted", "mic-unmuted"]:
            with open(f"/home/{self.user}/.config/dunst/icons/status/{status}.svg", "r", encoding="UTF-8") as file:
                data = file.readlines()
            data[mic_line] = f"""stroke="{color_config["wb-hvr-bg"]}"\n"""
            with open(f"/home/{self.user}/.config/dunst/icons/status/{status}.svg", "w", encoding="UTF-8") as file:
                file.writelines(data)

        for status in ["speaker-muted", "speaker-unmuted"]:
            with open(f"/home/{self.user}/.config/dunst/icons/status/{status}.svg", "r", encoding="UTF-8") as file:
                data = file.readlines()
            data[speaker_line] = f"""fill="{color_config["wb-hvr-bg"]}"\n"""
            with open(f"/home/{self.user}/.config/dunst/icons/status/{status}.svg", "w", encoding="UTF-8") as file:
                file.writelines(data)

        for status in ["lock-locked", "lock-unlocked"]:
            with open(f"/home/{self.user}/.config/dunst/icons/status/{status}.svg", "r", encoding="UTF-8") as file:
                data = file.readlines()
            data[lock_line] = f"""stroke="{color_config["wb-hvr-bg"]}"\n"""
            with open(f"/home/{self.user}/.config/dunst/icons/status/{status}.svg", "w", encoding="UTF-8") as file:
                file.writelines(data)

    def update_dunst(self, color_config, ulow_bckgrnd_line=294, ulow_frgrnd_line=295, ulow_fr_color_line=296, un_bckgrnd_line=301, un_frgrnd_line=302, un_fr_color_line=303):
        with open(f"/home/{self.user}/.config/dunst/dunstrc", "r", encoding="UTF-8") as file:
            data = file.readlines()
        data[ulow_bckgrnd_line] = f"""    background = "{color_config["main-bg"]}"\n"""
        data[ulow_frgrnd_line] = f"""    foreground = "{color_config["main-fg"]}"\n"""
        data[ulow_fr_color_line] = f"""    frame_color = "{color_config["wb-hvr-bg"]}"\n"""
        data[un_bckgrnd_line] = f"""    background = "{color_config["main-bg"]}"\n"""
        data[un_frgrnd_line] = f"""    foreground = "{color_config["main-fg"]}"\n"""
        data[un_fr_color_line] = f"""    frame_color = "{color_config["wb-hvr-bg"]}"\n"""
        with open(f"/home/{self.user}/.config/dunst/dunstrc", "w", encoding="UTF-8") as file:
            file.writelines(data)

        sp.run("killall dunst", shell=True)
        time.sleep(1)
        sp.run("dunst &", shell=True)

    def update_wlogout(self, theme):
        with open(f"/home/{self.user}/.config/wlogout/themes/theme.css", "w", encoding="UTF-8") as file:
            file.write(f'''@import "{theme}.css";''')

    def update_btop(self, theme, theme_line=4):
        with open(f"/home/{self.user}/.config/btop/btop.conf", "r", encoding="UTF-8") as file:
            data = file.readlines()
        data[theme_line] = f"""color_theme = "/home/{self.user}/.config/btop/themes/{theme}.theme"\n"""
        with open(f"/home/{self.user}/.config/btop/btop.conf", "w", encoding="UTF-8") as file:
            file.writelines(data)

    def apply_theme(self):
        config_theme, theme = self.rofi_select_theme()
        wallpaper, color_config = self.rofi_select_wallpaper(theme)
        self.change_wallpaper(wallpaper)
        self.update_hyprland(theme, theme, config_theme["cursor-theme"], config_theme["icon-theme"], config_theme["color-scheme"])
        self.update_kvantum(theme)
        self.update_qt5ct(theme, config_theme["icon-theme"])
        self.update_qt6ct(theme, config_theme["icon-theme"])
        self.update_gsettings(theme, config_theme["icon-theme"], config_theme["cursor-theme"], config_theme["color-scheme"])
        self.update_gtk_2(theme, config_theme["icon-theme"], config_theme["cursor-theme"])
        self.update_gtk_3(theme, config_theme["icon-theme"], config_theme["cursor-theme"])
        self.update_icons_default(config_theme["cursor-theme"])
        self.update_rofi(color_config)
        self.update_kitty(theme)
        self.update_waybar(color_config)
        self.update_wlogout(theme)
        self.update_btop(theme)
        self.update_notification_icons(color_config)
        self.update_dunst(color_config)


if __name__ == "__main__":
    manager = ThemeManager()
    manager.apply_theme()

