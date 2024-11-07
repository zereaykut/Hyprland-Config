#!/usr/bin/python
import subprocess as sp
import time

def waybar(color_config: dict, home: str) -> None:
    with open(f"{home}/.config/theme-manager/conf/waybar.css", "r", encoding="UTF-8") as f:
        waybar_theme = f.read()

    waybar_theme = waybar_theme.replace("""{{main-bg}}""", color_config["main-bg"])
    waybar_theme = waybar_theme.replace("""{{main-fg}}""", color_config["main-fg"])
    waybar_theme = waybar_theme.replace("""{{wb-act-bg}}""", color_config["wb-act-bg"])
    waybar_theme = waybar_theme.replace("""{{wb-act-fg}}""", color_config["wb-act-fg"])
    waybar_theme = waybar_theme.replace("""{{wb-hvr-bg}}""", color_config["wb-hvr-bg"])
    waybar_theme = waybar_theme.replace("""{{wb-hvr-fg}}""", color_config["wb-hvr-fg"])

    with open(f"{home}/.config/waybar/theme.css", "w", encoding="UTF-8") as file:
        file.write(waybar_theme)

    sp.run(["killall", "waybar"])
    time.sleep(0.5)
    sp.run("waybar &", shell=True)
    