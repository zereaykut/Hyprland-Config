#!/usr/bin/python


def rofi(config, color_config: dict, color_count: int, home: str) -> None:
    with open(f"{home}/.config/theme-manager/templates/rofi.rasi", "r", encoding="UTF-8") as f:
        rofi_theme = f.read()

    for i in range(color_count):
        rofi_theme = rofi_theme.replace(f"[[color{i}]]", color_config[f"color{i}"])

    rofi_theme = rofi_theme.replace("""[[icon-theme]]""", config["icon-theme"])

    with open(f"{home}/.config/rofi/theme.rasi", "w", encoding="UTF-8") as file:
        file.write(rofi_theme)
