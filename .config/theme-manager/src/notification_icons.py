#!/usr/bin/python


def status_icons(color_config: dict, status_icons_list: list[str], user: str) -> None:
    for icon in status_icons_list:
        with open(
            f"/home/{user}/.config/theme-manager/icons/status/{icon}.svg",
            "r",
            encoding="UTF-8",
        ) as f:
            data = f.read()
        print(color_config)
        data = data.replace("""{{wb-hvr-bg}}""", color_config["wb-hvr-bg"])

        with open(
            f"/home/{user}/.config/dunst/icons/status/{icon}.svg", "w", encoding="UTF-8"
        ) as file:
            file.write(data)


def vol_icons(color_config: dict, user: str) -> None:
    for vol in range(0, 101, 5):
        with open(
            f"/home/{user}/.config/theme-manager/icons/vol/vol-{vol}.svg",
            "r",
            encoding="UTF-8",
        ) as file:
            data = file.read()

        data = data.replace("""{{wb-hvr-fg}}""", color_config["wb-hvr-fg"])
        data = data.replace("""{{wb-hvr-bg}}""", color_config["wb-hvr-bg"])

        with open(
            f"/home/{user}/.config/dunst/icons/vol/vol-{vol}.svg", "w", encoding="UTF-8"
        ) as file:
            file.write(data)

