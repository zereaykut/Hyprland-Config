#!/usr/bin/python
import argparse
import subprocess as sp
import sys
import json

# %% Script statement
"""
    python brightness_control.py --action <parameter>
        << --action >>
            pacman  -> official arch updates
            yay     -> AUR updates
            pikaur  -> AUR updates
            trizen  -> AUR updates
            flatpak -> flatpak updates
    
    output:
        {
            "text": number of available updates
            "tooltip": available updates
        }
"""

# %% Argument
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--action", help="input to increase or decrease brightness by 5%")

args = parser.parse_args()
action = args.action

#%% Set Brightness
if action == "pacman":
    updates = sp.run("checkupdates", shell=True, capture_output=True, text=True,).stdout
elif action == "yay":
    updates = sp.run("yay -Qum", shell=True, capture_output=True, text=True,).stdout
elif action == "pikaur":
    updates = sp.run("pikaur -Qum", shell=True, capture_output=True, text=True,).stdout
elif action == "trizen":
    updates = sp.run("trizen -Qua", shell=True, capture_output=True, text=True,).stdout
elif action == "flatpak":
    updates = sp.run("flatpak remote-ls --updates", shell=True, capture_output=True, text=True,).stdout
else:
    sys.exit()

#%% Updates
updates = updates.strip()
if updates == "":
    text = "0"
else:
    updates = updates.split("\n")
    text = f"{len(updates)}"

tooltip = ""
for i in updates:
    if action == "flatpak":
        i = i.replace("\t", " ")
    
    if ".." in i:
        continue

    tooltip = f"{tooltip}\n{i}"

output = {
    "text": text,
    "tooltip": tooltip.strip()
}

print(json.dumps(output))