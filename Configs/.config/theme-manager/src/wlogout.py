#!/usr/bin/python


def wlogout(color_config: dict, color_count: int, home: str) -> None:
    with open(f"{home}/.config/theme-manager/templates/wlogout.css", "r", encoding="UTF-8") as f:
        wlogout_theme = f.read()

    for i in range(color_count):
            wlogout_theme = wlogout_theme.replace(f"[[color{i}]]", color_config[f"color{i}"])

    with open(f"{home}/.config/wlogout/theme.css", "w", encoding="UTF-8") as file:
        file.write(wlogout_theme)
