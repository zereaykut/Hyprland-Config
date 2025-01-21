#!/usr/bin/python
import os


def status_icons(color_config: dict, status_icons_list: list[str], color_count: int, home: str, notify_daemon: str) -> None:
    for icon in status_icons_list:
        with open(f"{home}/.config/theme-manager/icons/status/{icon}.svg", "r", encoding="UTF-8") as f:
            data = f.read()

        for i in range(color_count):
            data = data.replace(f"[[color{i}]]", color_config[f"color{i}"])
        
        os.makedirs(f"{home}/.config/{notify_daemon}/icons/status/", exist_ok=True)
        with open(f"{home}/.config/{notify_daemon}/icons/status/{icon}.svg", "w", encoding="UTF-8") as file:
            file.write(data)


def vol_icons(color_config: dict, color_count: int, home: str, notify_daemon: str) -> None:
    for vol in range(0, 101, 5):
        with open(f"{home}/.config/theme-manager/icons/vol/vol-{vol}.svg", "r", encoding="UTF-8") as file:
            data = file.read()

        for i in range(color_count):
            data = data.replace(f"[[color{i}]]", color_config[f"color{i}"])

        os.makedirs(f"{home}/.config/{notify_daemon}/icons/vol/", exist_ok=True)
        with open(f"{home}/.config/{notify_daemon}/icons/vol/vol-{vol}.svg", "w", encoding="UTF-8") as file:
            file.write(data)

