#!/usr/bin/python


def wlogout(color_config: dict, home: str) -> None:
    with open(f"{home}/.config/theme-manager/conf/wlogout.css", "r", encoding="UTF-8") as f:
        wlogout_theme = f.read()

    wlogout_theme = wlogout_theme.replace("""{{main-bg}}""", color_config["main-bg"])
    wlogout_theme = wlogout_theme.replace("""{{main-fg}}""", color_config["main-fg"])
    wlogout_theme = wlogout_theme.replace(
        """{{wb-act-bg}}""", color_config["wb-act-bg"]
    )
    wlogout_theme = wlogout_theme.replace(
        """{{wb-act-fg}}""", color_config["wb-act-fg"]
    )
    wlogout_theme = wlogout_theme.replace(
        """{{wb-hvr-bg}}""", color_config["wb-hvr-bg"]
    )
    wlogout_theme = wlogout_theme.replace(
        """{{wb-hvr-fg}}""", color_config["wb-hvr-fg"]
    )

    with open(f"{home}/.config/wlogout/theme.css", "w", encoding="UTF-8") as file:
        file.write(wlogout_theme)
