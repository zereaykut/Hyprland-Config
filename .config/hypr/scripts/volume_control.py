#!/usr/bin/python
import argparse
import subprocess as sp
import sys

# %% Script statement
"""
    python volume_control.py --action <parameter> --device <parameter>
        << --action >>
            i: increase volume by 5%
            d: decrease volume by 5%
            m: toggle mute and unmute volume
        << --device >>
            i: input device
            o: output device
"""

#%% User
user = sp.run("whoami", shell=True, capture_output=True, text=True,).stdout.strip()

# %% Argument
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--action", help="input to increase or decrease volume by 5%")
parser.add_argument("-d", "--device", help="input to increase or decrease volume by 5%")
args = parser.parse_args()
action = args.action
device = args.device

if device == "i":
    src = "--default-source"
elif device == "o":
    src = ""
else:
    sys.exit()

#%% Set volume
if action == "i":
    sp.run(f"pamixer {src} -i 5", shell=True)
elif action == "d":
    sp.run(f"pamixer {src} -d 5", shell=True)
elif action == "m":
    sp.run(f"pamixer {src} -t", shell=True)
else:
    sys.exit()

#%% Send Notification
if action == "m":
    mute_state = sp.run(f"pamixer {src} --get-mute", shell=True, capture_output=True, text=True,).stdout.strip()
    if mute_state == "true":
        if device == "o":
            icon = f"/home/{user}/.config/dunst/icons/status/speaker-muted.svg"
            sp.run(f"""dunstify "Speaker is muted" -i {icon} -r 91190 -t 800 -u normal""", shell=True)
        elif device == "i":
            icon = f"/home/{user}/.config/dunst/icons/status/mic-muted.svg"
            sp.run(f"""dunstify "Microphone is muted" -i {icon} -r 91190 -t 800 -u normal""", shell=True)
        else:
            sys.exit()
    else:
        if device == "o":
            icon = f"/home/{user}/.config/dunst/icons/status/speaker-unmuted.svg"
            sp.run(f"""dunstify "Speaker is unmuted" -i {icon} -r 91190 -t 800 -u normal""", shell=True)
        elif device == "i":
            icon = f"/home/{user}/.config/dunst/icons/status/mic-unmuted.svg"
            sp.run(f"""dunstify "Microphone is unmuted" -i {icon} -r 91190 -t 800 -u normal""", shell=True)
        else:
            sys.exit()

else:
    volume_percent = int(sp.run(f"pamixer {src} --get-volume", shell=True, capture_output=True, text=True,).stdout.strip())
    volume_vol = volume_percent//5*5
    icon = f"/home/{user}/.config/dunst/icons/vol/vol-{volume_vol}.svg"
    sp.run(f"""dunstify "Volume {volume_percent}%" -i {icon} -r 91190 -t 800 -u normal""", shell=True)

