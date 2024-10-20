#!/usr/bin/python


def btop(theme: str, user: str) -> None:
    with open(
        f"/home/{user}/.config/theme-manager/conf/btop.conf", "r", encoding="UTF-8"
    ) as f:
        btop_config = f.read()

    btop_config = btop_config.replace(
        """{{theme}}""", f"""/home/{user}/.config/btop/themes/{theme}.theme"""
    )

    with open(f"/home/{user}/.config/btop/btop.conf", "w", encoding="UTF-8") as file:
        file.write(btop_config)
