#!/usr/bin/python


def rofi(color_config: dict, user: str) -> None:
    with open(
        f"/home/{user}/.config/theme-manager/conf/rofi.rasi", "r", encoding="UTF-8"
    ) as f:
        rofi_theme = f.read()

    rofi_theme = rofi_theme.replace("""{{main-bg}}""", color_config["main-bg"])
    rofi_theme = rofi_theme.replace("""{{main-fg}}""", color_config["main-fg"])
    rofi_theme = rofi_theme.replace("""{{wb-hvr-bg}}""", color_config["wb-hvr-bg"])
    rofi_theme = rofi_theme.replace("""{{wb-act-bg}}""", color_config["wb-act-bg"])
    rofi_theme = rofi_theme.replace("""{{wb-hvr-fg}}""", color_config["wb-hvr-fg"])

    with open(f"/home/{user}/.config/rofi/theme.rasi", "w", encoding="UTF-8") as file:
        file.write(rofi_theme)
