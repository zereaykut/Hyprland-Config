#!/usr/bin/python
import argparse
import subprocess as sp
import sys

# %% Script statement
"""
    python brightness_control.py --action <parameter>
        << --action >>
            i: increase brightness by 5%
            d: decrease brightness by 5%
"""

#%% User
user = sp.run("whoami", shell=True, capture_output=True, text=True,).stdout.strip()

# %% Argument
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--action", help="input to increase or decrease brightness by 5%")

args = parser.parse_args()
action = args.action

#%% Set Brightness
if action == "i":
    sp.run("brightnessctl set +5%", shell=True)
elif action == "d":
    sp.run("brightnessctl set 5%-", shell=True)
else:
    sys.exit()

#%% Send Notification
brightness_val = int(sp.run("brightnessctl get", shell=True, capture_output=True, text=True,).stdout.strip())
brightness_max = int(sp.run("brightnessctl max", shell=True, capture_output=True, text=True,).stdout.strip())
brightness_percent = int(brightness_val/brightness_max * 100)
brightness_vol = brightness_percent//5*5
icon = f"/home/{user}/.config/dunst/icons/vol/vol-{brightness_vol}.svg"

sp.run(f"""dunstify "Brightness {brightness_percent}%" -i {icon} -r 91190 -t 800 -u normal""", shell=True)

