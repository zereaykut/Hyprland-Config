#!/usr/bin/python
import subprocess as sp


def hyprland(config: dict, color_config: dict, theme: str, cursor_size: int, color_count: int, home: str) -> None:
    with open(f"{home}/.config/theme-manager/templates/hyprland_colors.conf", "r", encoding="UTF-8") as f:
        hyprland_colors = f.read()

    for i in range(color_count):
        hyprland_colors = hyprland_colors.replace(f"[[color{i}]]", color_config[f"color{i}"].replace("#", "") + "ff")

    with open(f"{home}/.config/hypr/confs/colors.conf", "w", encoding="UTF-8") as file:
        file.write(hyprland_colors)


    with open(f"{home}/.config/theme-manager/templates/hyprland_theme.conf", "r", encoding="UTF-8") as f:
        hyprland_theme_config = f.read()

    hyprland_theme_config = hyprland_theme_config.replace("""[[theme]]""", theme)
    hyprland_theme_config = hyprland_theme_config.replace("""[[icon-theme]]""", config["icon-theme"])
    hyprland_theme_config = hyprland_theme_config.replace("""[[cursor-theme]]""", config["cursor-theme"])
    hyprland_theme_config = hyprland_theme_config.replace("""[[cursor-size]]""", str(cursor_size))

    with open(f"{home}/.config/hypr/confs/theme.conf", "w", encoding="UTF-8") as file:
        file.write(hyprland_theme_config)

    sp.run(["hyprctl", "setcursor", config["cursor-theme"], str(cursor_size)])
    sp.run(["hyprctl", "reload"])
