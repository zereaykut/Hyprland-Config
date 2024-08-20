#!/usr/bin/python
import os
import subprocess as sp
import json

from src.btop import btop
from src.dunstrc import dunstrc
from src.gtk import gtk2, gtk3, gsettings, default_icons
from src.hyprland import hyprland
from src.kitty import kitty
from src.kvantum import kvantum
from src.nwg_icons import nwg_icons
from src.qt import qt5ct, qt6ct
from src.rofi import rofi
from src.swww import swww
from src.waybar import waybar
from src.wlogout import wlogout
from src.notification_icons import mic_unmuted, mic_muted, speaker_unmuted, speaker_muted, lock_unlocked, lock_locked, wifi_enabled, wifi_disabled, vol_icons

class ThemeManager:
    def __init__(self):
        self.user = sp.run("whoami", shell=True, capture_output=True, text=True).stdout.strip()
        self.config = self.get_config()

    def get_config(self):
        with open(f"/home/{self.user}/.config/theme-manager/themes_config.json", "r") as f:
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

    def apply_theme(self):
        config_theme, theme = self.rofi_select_theme()
        wallpaper, color_config = self.rofi_select_wallpaper(theme)
        swww(wallpaper, self.user)
        hyprland(config_theme, color_config, theme, self.user)
        kvantum(theme, self.user)
        qt5ct(config_theme, theme, self.user)
        qt6ct(config_theme, theme, self.user)
        gsettings(config_theme, theme, self.user)
        gtk2(config_theme, theme, self.user)
        gtk3(config_theme, theme, self.user)
        rofi(color_config, self.user)
        kitty(theme, self.user)
        waybar(color_config, self.user)
        wlogout(color_config, self.user)
        btop(theme, self.user)
        mic_unmuted(color_config, self.user)
        mic_muted(color_config, self.user)
        speaker_unmuted(color_config, self.user)
        speaker_muted(color_config, self.user)
        lock_unlocked(color_config, self.user)
        lock_locked(color_config, self.user)
        wifi_enabled(color_config, self.user)
        wifi_disabled(color_config, self.user)
        vol_icons(color_config, self.user)
        dunstrc(color_config, self.user)


if __name__ == "__main__":
    manager = ThemeManager()
    manager.apply_theme()

