#!/usr/bin/python

def nwg_icons(config, theme, user):
    nwg_icons_config = [
        "[Icon Theme]",
        "Name=Default",
        "Comment=Default Cursor Theme",
        f"""Inherits={config["cursor-theme"]}"""
        ]

    with open(f"/home/{user}/.icons/default/index.theme", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(nwg_icons_config))
