#!/usr/bin/python
import os
import subprocess as sp
import json

from src.sddm import sddm
from theme_manager import ThemeManager

class ThemeManagerSDDM(ThemeManager):
    def __init__(self):
        super().__init__()
    
    def apply_theme(self):
        config_theme, theme = self.rofi_select_theme()
        with open(f"/home/{self.user}/.cache/color_schemes/Lock-Screen/{theme}.json", "r") as f:
            color_config = json.load(f)
        sddm(config_theme, color_config, theme, self.user, screen_width=1920, screen_height=1080)
        sp.run(f"bash /home/{self.user}/.config/theme-manager/run/sddm.sh", shell=True)


if __name__ == "__main__":
    manager = ThemeManagerSDDM()
    manager.apply_theme()
