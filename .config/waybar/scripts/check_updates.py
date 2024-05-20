#!/usr/bin/python
import argparse
import subprocess as sp
import sys

# %% Script statement
"""
    python brightness_control.py --action <parameter>
        << --action >>
            pacman
            yay
            pikaur
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
else:
    sys.exit()

#%% Updates
updates = updates.split("\n")
# print(updates.split("\n"))
output = f"{len(updates)}"
for i in updates:
    if ".." in i:
        pass
    else:
        output = f"{output}\n{i}"
print(output)