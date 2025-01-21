#!/usr/bin/python


def kdeglobals(config: dict, home: str) -> None:
    with open(f"{home}/.config/theme-manager/templates/kdeglobals", "r", encoding="UTF-8") as f:
        kdeglobals_config = f.read()

    kdeglobals_config = kdeglobals_config.replace("""[[icon-theme]]""", config["icon-theme"])

    with open(f"{home}/.config/kdeglobals", "w", encoding="UTF-8") as file:
        file.write(kdeglobals_config)

