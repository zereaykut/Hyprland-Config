#!/usr/bin/python
import json
import subprocess as sp


def main():

    powerprofile = sp.run(["powerprofilesctl", "get"], capture_output=True, text=True).stdout.strip()

    text, tooltip = None, None

    if powerprofile == "performance":
        text = ""
        tooltip = " Performance"

    elif powerprofile == "balanced":
        text = ""
        tooltip = " Balanced"

    elif powerprofile == "power-saver":
        text = ""
        tooltip = " Power-Saver"

    output = {"text": text, "tooltip": tooltip}

    print(json.dumps(output))


if __name__ == "__main__":
    main()
