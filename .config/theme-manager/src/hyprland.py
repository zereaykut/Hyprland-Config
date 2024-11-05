#!/usr/bin/python
import subprocess as sp


def hyprland(
    config: dict, color_config: dict, theme: str, cursor_size: int, user: str
) -> None:
    with open(
        f"/home/{user}/.config/theme-manager/conf/hyprland_theme.conf",
        "r",
        encoding="UTF-8",
    ) as f:
        hyprland_theme_config = f.read()

    hyprland_theme_config = hyprland_theme_config.replace("""{{theme}}""", theme)
    hyprland_theme_config = hyprland_theme_config.replace(
        """{{icon-theme}}""", config["icon-theme"]
    )
    hyprland_theme_config = hyprland_theme_config.replace(
        """{{cursor-theme}}""", config["cursor-theme"]
    )
    hyprland_theme_config = hyprland_theme_config.replace(
        """{{cursor-size}}""", str(cursor_size)
    )

    hyprland_theme_config = hyprland_theme_config.replace(
        """{{wb-hvr-bg}}""", f"""{color_config["wb-hvr-bg"].replace("#", "")}ff"""
    )
    hyprland_theme_config = hyprland_theme_config.replace(
        """{{main-fg}}""", f"""{color_config["main-fg"].replace("#", "")}ff"""
    )

    hyprland_theme_config = hyprland_theme_config.replace(
        """{{main-bg}}""", f"""{color_config["main-bg"].replace("#", "")}ff"""
    )
    hyprland_theme_config = hyprland_theme_config.replace(
        """{{wb-hvr-fg}}""", f"""{color_config["wb-hvr-fg"].replace("#", "")}ff"""
    )

    with open(
        f"/home/{user}/.config/hypr/confs/theme.conf", "w", encoding="UTF-8"
    ) as file:
        file.write(hyprland_theme_config)

    sp.run(["hyprctl", "setcursor", config["cursor-theme"], str(cursor_size)])
    sp.run(["hyprctl", "reload"])
