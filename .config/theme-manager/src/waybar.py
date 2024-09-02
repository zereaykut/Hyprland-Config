#!/usr/bin/python
import subprocess as sp

def waybar(color_config, user):
    with open(f"/home/{user}/.config/theme-manager/conf/waybar.css", "r", encoding="UTF-8") as f:
        waybar_theme = f.read()

    waybar_theme = waybar_theme.replace("""{{main-bg}}""", color_config["main-bg"])
    waybar_theme = waybar_theme.replace("""{{main-fg}}""", color_config["main-fg"])
    waybar_theme = waybar_theme.replace("""{{wb-act-bg}}""", color_config["wb-act-bg"])
    waybar_theme = waybar_theme.replace("""{{wb-act-fg}}""", color_config["wb-act-fg"])
    waybar_theme = waybar_theme.replace("""{{wb-hvr-bg}}""", color_config["wb-hvr-bg"])
    waybar_theme = waybar_theme.replace("""{{wb-hvr-fg}}""", color_config["wb-hvr-fg"])

    with open(f"/home/{user}/.config/waybar/theme.css", "w", encoding="UTF-8") as file:
        file.write(waybar_theme)
    
    sp.run(f"bash /home/{user}/.config/theme-manager/run/waybar.sh", shell=True)

