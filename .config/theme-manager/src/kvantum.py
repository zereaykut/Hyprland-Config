#!/usr/bin/python

def kvantum(theme, user):
    kvantum_config = [
        "[General]",
        f"theme={theme}"
    ]
    with open(f"/home/{user}/.config/Kvantum/kvantum.kvconfig", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(kvantum_config))

