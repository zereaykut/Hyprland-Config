#!/usr/bin/python
import json
import os
import subprocess as sp
from pathlib import Path

from src.btop import btop
from src.dunst import dunst
from src.flatpak import flatpak
from src.gtk import gsettings, gtk2, gtk3
from src.hyprland import hyprland
from src.hyprlock import hyprlock
from src.kdeglobals import kdeglobals
from src.kitty import kitty
from src.kvantum import kvantum
from src.notification_icons import status_icons, vol_icons
from src.notify import send_notification
from src.qt import qt5ct, qt6ct
from src.rofi import rofi
from src.swww import swww
from src.waybar import waybar
from src.wlogout import wlogout


class ThemeManager:
    def __init__(self):
        self.home = str(Path.home())
        self.config = self.get_config()

    def get_config(self):
        with open(f"{self.home}/.config/theme-manager/themes_config.json", "r", encoding="UTF-8") as f:
            return json.load(f)

    def rofi_select_theme(self):
        themes = os.listdir(f"""{self.home}/.config/wallpapers/Lock-Screen""")
        themes = sorted(themes)
        if os.path.exists(f"{self.home}/.cache/theme-manager/wallpapers/Lock-Screen/"):
            rofi_output = [
                f"""{wall.split(".")[0]}\\0icon\\x1f/{self.home}/.cache/theme-manager/wallpapers/Lock-Screen/{wall}"""
                for wall in themes
            ]
        else:
            rofi_output = [
                f"""{wall.split(".")[0]}\\0icon\\x1f/{self.home}/.config/wallpapers/Lock-Screen/{wall}"""
                for wall in themes
            ]
        rofi_output = "\n".join(rofi_output)
        rofi_select = sp.run(
            f"""echo -en "{rofi_output}" | rofi -dmenu -matching normal -i -theme ~/.config/rofi/theme_select.rasi""",
            shell=True,
            capture_output=True,
            text=True,
        )
        rofi_selected = rofi_select.stdout.strip()
        return self.config[rofi_selected], rofi_selected

    def rofi_select_wallpaper(self, theme: str):
        wallpapers = os.listdir(f"""{self.home}/.config/wallpapers/{theme}""")
        wallpapers = sorted(wallpapers)
        if os.path.exists(f"{self.home}/.cache/theme-manager/wallpapers/{theme}/"):
            rofi_output = [
                f"""{wall}\\0icon\\x1f/{self.home}/.cache/theme-manager/wallpapers/{theme}/{wall}"""
                for wall in wallpapers
            ]
        else:
            rofi_output = [
                f"""{wall}\\0icon\\x1f/{self.home}/.config/wallpapers/{theme}/{wall}"""
                for wall in wallpapers
            ]
        rofi_output = "\n".join(rofi_output)
        rofi_select = sp.run(
            f"""echo -en "{rofi_output}" | rofi -dmenu -matching normal -i -theme ~/.config/rofi/wallpaper_select.rasi""",
            shell=True,
            capture_output=True,
            text=True,
        )
        wallpaper = rofi_select.stdout.strip()
        color_scheme = wallpaper.rsplit(".", 1)[0]
        with open(f"{self.home}/.cache/theme-manager/color-schemes/{theme}/{color_scheme}.json", "r", encoding="UTF-8") as f:
            color_config = json.load(f)
        return f"{self.home}/.config/wallpapers/{theme}/{wallpaper}", color_config

    def apply_theme(self):
        cursor_size = 24
        config_theme, theme = self.rofi_select_theme()
        wallpaper, color_config = self.rofi_select_wallpaper(theme)
        swww(wallpaper)
        hyprland(config_theme, color_config, theme, cursor_size, self.home)
        hyprlock(theme, self.home)
        kvantum(theme, self.home)
        qt5ct(config_theme, theme, self.home)
        qt6ct(config_theme, theme, self.home)
        kdeglobals(config_theme, self.home)
        gsettings(config_theme, theme, self.home, cursor_size)
        gtk2(config_theme, theme, cursor_size, self.home)
        gtk3(config_theme, theme, cursor_size, self.home)
        rofi(config_theme, color_config, self.home)
        kitty(theme, self.home)
        waybar(color_config, self.home)
        wlogout(color_config, self.home)
        btop(theme, self.home)
        flatpak(config_theme, theme)
        status_icons(
            color_config,
            [
                "mic-unmuted",
                "mic-muted",
                "speaker-unmuted",
                "speaker-muted",
                "lock-unlocked",
                "lock-locked",
                "wifi-disabled",
                "wifi-enabled",
                "palette",
                "charger-plugged",
                "charger-not-plugged",
                "clip",
                "clip-edit"
            ],
            self.home,
            "dunst"
        )
        vol_icons(color_config, self.home, "dunst")
        dunst(color_config, self.home)

        wall_name = wallpaper.split("/")[-1].split(".")[0]
        send_notification(
            f"Theme: {theme}\nWallpaper: {wall_name}",
            f"{self.home}/.config/dunst/icons/status/palette.svg",
            2000,
        )


if __name__ == "__main__":
    manager = ThemeManager()
    manager.apply_theme()
