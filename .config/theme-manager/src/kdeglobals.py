#!/usr/bin/python


def kdeglobals(config: dict, user: str) -> None:
    with open(
        f"/home/{user}/.config/theme-manager/conf/kdeglobals", "r", encoding="UTF-8"
    ) as f:
        kdeglobals_config = f.read()

    kdeglobals_config = kdeglobals_config.replace(
        """{{icon-theme}}""", config["icon-theme"]
    )

    with open(f"/home/{user}/.config/kdeglobals", "w", encoding="UTF-8") as file:
        file.write(kdeglobals_config)

