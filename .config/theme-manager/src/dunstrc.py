#!/usr/bin/python
import subprocess as sp


def dunstrc(color_config: dict, user: str) -> None:
    with open(
        f"/home/{user}/.config/theme-manager/conf/dunstrc", "r", encoding="UTF-8"
    ) as f:
        dunsrc_config = f.read()

    dunsrc_config = dunsrc_config.replace("""{{main-bg}}""", color_config["main-bg"])
    dunsrc_config = dunsrc_config.replace("""{{main-fg}}""", color_config["main-fg"])
    dunsrc_config = dunsrc_config.replace(
        """{{wb-hvr-bg}}""", color_config["wb-hvr-bg"]
    )

    with open(f"/home/{user}/.config/dunst/dunstrc", "w", encoding="UTF-8") as file:
        file.write(dunsrc_config)

    sp.run(f"bash /home/{user}/.config/theme-manager/run/dunst.sh", shell=True)
