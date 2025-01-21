#!/usr/bin/python
import subprocess as sp
import time

def waybar(color_config: dict, color_count: int, home: str) -> None:
    with open(f"{home}/.config/theme-manager/templates/waybar.css", "r", encoding="UTF-8") as f:
        waybar_theme = f.read()

    for i in range(color_count):
        waybar_theme = waybar_theme.replace(f"[[color{i}]]", color_config[f"color{i}"])

    with open(f"{home}/.config/waybar/theme.css", "w", encoding="UTF-8") as file:
        file.write(waybar_theme)

    sp.run(["killall", "waybar"])
    time.sleep(0.5)
    sp.run("waybar &", shell=True)
    