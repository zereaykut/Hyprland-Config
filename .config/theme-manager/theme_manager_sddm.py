#!/usr/bin/python
import os
import json

from src.sddm import sddm
from theme_manager import ThemeManager

class ThemeManagerSDDM(ThemeManager):
    def __init__(self):
        super().__init__()
    
    def apply_theme(self):
        cursor_size = 24
        config_theme, theme = self.rofi_select_theme()
        with open(f"/home/{self.user}/.cache/color_schemes/Lock-Screen/{theme}.json", "r") as f:
            color_config = json.load(f)
        sddm(config_theme, color_config, theme, cursor_size, self.user, screen_width=1920, screen_height=1080)


if __name__ == "__main__":
    manager = ThemeManagerSDDM()
    manager.apply_theme()

