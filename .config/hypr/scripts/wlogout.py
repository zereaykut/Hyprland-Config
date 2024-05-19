#!/usr/bin/python
import argparse
import subprocess as sp
import sys

# %% Script statement
"""
    python brightness_control.py --resolution <parameter> --scale <parameter>
        << --resolution >>
            resolution: integer as an example 1080
        << --scale >>
            scale: integer value as an example 1
"""

margin = 400

# %% Argument
parser = argparse.ArgumentParser()
parser.add_argument("-r", "--resolution", help="monitor resolution as integer, ex. 1080")
parser.add_argument("-s", "--scale", help="monitor resolution as integer, ex. 1")

args = parser.parse_args()
resolution = args.resolution
scale = args.scale

#%% Wlogout
try:
    resolution = int(resolution)
    scale = int(scale)
    margin = margin * 1080 * scale/resolution
    sp.run(f"""wlogout -b 6 -T {margin} -B {margin}""", shell=True)
except Exception as e:
    print(e)
    sys.exit()

