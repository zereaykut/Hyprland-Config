#!/usr/bin/python
import subprocess as sp


def flatpak(config: dict, theme: str, user: str) -> None:
    sp.run(["flatpak", "--user override", f'--env=GTK_THEME="{theme}"'])
    sp.run(["flatpak", "--user", "override", f'--env=ICON_THEME="{config["icon-theme"]}"'])
