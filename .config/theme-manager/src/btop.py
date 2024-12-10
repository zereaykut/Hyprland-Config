#!/usr/bin/python


def btop(theme: str, home: str) -> None:
    with open(f"{home}/.config/theme-manager/templates/btop.conf", "r", encoding="UTF-8") as f:
        btop_config = f.read()

    btop_config = btop_config.replace("""[[theme]]""", f"""{home}/.config/btop/themes/{theme}.theme""")

    with open(f"{home}/.config/btop/btop.conf", "w", encoding="UTF-8") as file:
        file.write(btop_config)
