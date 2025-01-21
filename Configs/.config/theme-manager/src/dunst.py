#!/usr/bin/python
import subprocess as sp
import time

def dunst(color_config: dict, color_count: int, home: str) -> None:
    with open(f"{home}/.config/theme-manager/templates/dunstrc", "r", encoding="UTF-8") as f:
        dunsrc_config = f.read()

    for i in range(color_count):
        dunsrc_config = dunsrc_config.replace(f"""[[color{i}]]""", color_config[f"color{i}"])

    with open(f"{home}/.config/dunst/dunstrc", "w", encoding="UTF-8") as file:
        file.write(dunsrc_config)

    sp.run(["killall", "dunst"])
    time.sleep(0.5)
    sp.run("dunst &", shell=True)
    