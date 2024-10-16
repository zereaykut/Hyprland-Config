#!/usr/bin/python
import json
import os
import subprocess as sp

from src.btop import btop
from src.dunstrc import dunstrc, send_notification
from src.flatpak import flatpak
from src.gtk import gsettings, gtk2, gtk3
from src.hyprland import hyprland
from src.hyprlock import hyprlock
from src.kdeglobals import kdeglobals
from src.kitty import kitty
from src.kvantum import kvantum
from src.notification_icons import status_icons, vol_icons
from src.qt import qt5ct, qt6ct
from src.rofi import rofi
from src.swww import swww
from src.waybar import waybar
from src.wlogout import wlogout


class ThemeManager:
    def __init__(self):
        self.user = sp.run(
            "whoami", shell=True, capture_output=True, text=True
        ).stdout.strip()
        self.config = self.get_config()

    def get_config(self):
        with open(
            f"/home/{self.user}/.config/theme-manager/themes_config.json",
            "r",
            encoding="UTF-8",
        ) as f:
            return json.load(f)

    def rofi_select_theme(self):
        themes = os.listdir(f"""/home/{self.user}/.config/wallpapers/Lock-Screen""")
        themes = sorted(themes)
        if os.path.exists(
            f"/home/{self.user}/.cache/theme-manager/wallpapers/Lock-Screen/"
        ):
            rofi_output = [
                f"""{wall.split(".")[0]}\\0icon\\x1f/home/{self.user}/.cache/theme-manager/wallpapers/Lock-Screen/{wall}"""
                for wall in themes
            ]
        else:
            rofi_output = [
                f"""{wall.split(".")[0]}\\0icon\\x1f/home/{self.user}/.config/wallpapers/Lock-Screen/{wall}"""
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
        wallpapers = os.listdir(f"""/home/{self.user}/.config/wallpapers/{theme}""")
        wallpapers = sorted(wallpapers)
        if os.path.exists(
            f"/home/{self.user}/.cache/theme-manager/wallpapers/{theme}/"
        ):
            rofi_output = [
                f"""{wall}\\0icon\\x1f/home/{self.user}/.cache/theme-manager/wallpapers/{theme}/{wall}"""
                for wall in wallpapers
            ]
        else:
            rofi_output = [
                f"""{wall}\\0icon\\x1f/home/{self.user}/.config/wallpapers/{theme}/{wall}"""
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
        with open(
            f"/home/{self.user}/.cache/theme-manager/color-schemes/{theme}/{color_scheme}.json",
            "r",
            encoding="UTF-8",
        ) as f:
            color_config = json.load(f)
        return f"/home/{self.user}/.config/wallpapers/{theme}/{wallpaper}", color_config

    def apply_theme(self):
        cursor_size = 24
        config_theme, theme = self.rofi_select_theme()
        wallpaper, color_config = self.rofi_select_wallpaper(theme)
        swww(wallpaper, self.user)
        hyprland(config_theme, color_config, theme, cursor_size, self.user)
        hyprlock(theme, self.user)
        kvantum(theme, self.user)
        qt5ct(config_theme, theme, self.user)
        qt6ct(config_theme, theme, self.user)
        kdeglobals(config_theme, self.user)
        gsettings(config_theme, theme, self.user)
        gtk2(config_theme, theme, cursor_size, self.user)
        gtk3(config_theme, theme, cursor_size, self.user)
        rofi(color_config, self.user)
        kitty(theme, self.user)
        waybar(color_config, self.user)
        wlogout(color_config, self.user)
        btop(theme, self.user)
        flatpak(config_theme, theme, self.user)
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
            ],
            self.user,
        )
        vol_icons(color_config, self.user)
        dunstrc(color_config, self.user)

        wall_name = wallpaper.split("/")[-1].split(".")[0]
        send_notification(
            f"Theme: {theme}\nWallpaper: {wall_name}",
            f"/home/{self.user}/.config/dunst/icons/status/palette.svg",
            2000,
        )


if __name__ == "__main__":
    manager = ThemeManager()
    manager.apply_theme()
