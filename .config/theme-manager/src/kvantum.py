#!/usr/bin/python


def kvantum(theme: str, home: str) -> None:
    with open(f"{home}/.config/theme-manager/templates/kvantum.kvconfig", "r", encoding="UTF-8") as f:
        kvantum_kvconfig = f.read()

    kvantum_kvconfig = kvantum_kvconfig.replace("""[[theme]]""", theme)

    with open(f"{home}/.config/Kvantum/kvantum.kvconfig", "w", encoding="UTF-8") as file:
        file.write(kvantum_kvconfig)
