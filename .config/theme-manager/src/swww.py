#!/usr/bin/python
import subprocess as sp


def swww(wallpaper: str) -> None:
    sp.run(["swww", "img", wallpaper, "--transition-type", "center", "--transition-fps", "60", "--transition-duration" , "3"])
