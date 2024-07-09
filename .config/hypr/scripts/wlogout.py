#!/usr/bin/python
import argparse
import subprocess as sp
import sys

class WLogout:
    def __init__(self, resolution, scale):
        self.margin = 400
        self.resolution = resolution
        self.scale = scale

    def calculate_margin(self):
        try:
            self.resolution = int(self.resolution)
            self.scale = int(self.scale)
            self.margin = self.margin * 1080 * self.scale / self.resolution
        except ValueError as e:
            print(f"Invalid input: {e}")
            sys.exit(1)

    def execute_wlogout(self):
        try:
            self.calculate_margin()
            sp.run(f"wlogout -b 6 -T {self.margin} -B {self.margin}", shell=True)
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)

def main():
    """
    python wlogout.py --resolution <parameter> --scale <parameter>
        << --resolution >>
            resolution: integer as an example 1080
        << --scale >>
            scale: integer value as an example 1
    """

    parser = argparse.ArgumentParser(description="Run wlogout with specified resolution and scale.")
    parser.add_argument("-r", "--resolution", help="Monitor resolution as integer, ex. 1080", required=True)
    parser.add_argument("-s", "--scale", help="Monitor scale as integer, ex. 1", required=True)

    args = parser.parse_args()

    wlogout = WLogout(args.resolution, args.scale)
    wlogout.execute_wlogout()

if __name__ == "__main__":
    main()
