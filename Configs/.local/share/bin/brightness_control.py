#!/usr/bin/python
import argparse
import subprocess as sp
import sys


class BrightnessControl:
    def __init__(self, action):
        self.user = sp.run(["whoami"], capture_output=True, text=True).stdout.strip()
        self.action = action

    def set_brightness(self):
        if self.action == "i":
            sp.run(["brightnessctl", "set", "+5%"])
        elif self.action == "d":
            sp.run(["brightnessctl", "set", "5%-"])
        else:
            sys.exit("Invalid action parameter")

    def send_notification(self):
        brightness_val = int(sp.run(["brightnessctl", "get"], capture_output=True, text=True).stdout.strip())
        brightness_max = int(sp.run(["brightnessctl", "max"], capture_output=True, text=True).stdout.strip())
        brightness_percent = int(brightness_val / brightness_max * 100)
        brightness_vol = brightness_percent // 5 * 5
        icon = f"/home/{self.user}/.config/dunst/icons/vol/vol-{brightness_vol}.svg"

        sp.run(["notify-send", f"Brightness {brightness_percent}%", "-i", icon, "-r", "91190", "-t", "800", "-u", "normal"])


def main():
    """
    python brightness_control.py --action <parameter>
        << --action >>
            i: increase brightness by 5%
            d: decrease brightness by 5%
    """

    parser = argparse.ArgumentParser(
        description="Control brightness and send notifications."
    )
    parser.add_argument(
        "-a",
        "--action",
        help="Action to increase or decrease brightness by 5%",
        required=True,
    )

    args = parser.parse_args()

    brightness_control = BrightnessControl(args.action)
    brightness_control.set_brightness()
    brightness_control.send_notification()


if __name__ == "__main__":
    main()
