#!/usr/bin/python
import subprocess as sp

def waybar(color_config, user):
    waybar_theme = [
        f"""@define-color main-bg {color_config["main-bg"]};""",
        f"""@define-color main-fg {color_config["main-fg"]};""",
        f"""@define-color wb-act-bg {color_config["wb-act-bg"]};""",
        f"""@define-color wb-act-fg {color_config["wb-act-fg"]};""",
        f"""@define-color wb-hvr-bg {color_config["wb-hvr-bg"]};""",
        f"""@define-color wb-hvr-fg {color_config["wb-hvr-fg"]};"""
        ]
    with open(f"/home/{user}/.config/waybar/theme.css", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(waybar_theme))
    
    sp.run(f"bash /home/{user}/.config/theme-manager/run/waybar.sh", shell=True)
