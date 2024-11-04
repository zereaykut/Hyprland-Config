#!/usr/bin/python
import argparse
import subprocess as sp
import sys
import json

# Usage
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

class BrightnessControl:
    def __init__(self, action):
        self.action = action
        self.updates = ""
        self.text = ""
        self.tooltip = ""

    def check_updates(self):
        """Run the update check based on the specified action."""
        commands = {
            "pacman": ["checkupdates"],
            "yay": ["yay", "-Qum"],
            "pikaur": ["pikaur", "-Qum"],
            "trizen": ["trizen", "-Qua"],
            "flatpak": ["flatpak", "remote-ls", "--updates"]
        }
        
        if self.action in commands:
            self.updates = sp.run(commands[self.action], capture_output=True, text=True).stdout.strip()
        else:
            sys.exit("Invalid action specified")

    def parse_updates(self):
        """Parse the output of the update command to prepare text and tooltip."""
        if not self.updates:
            self.text = "0"
            self.tooltip = "No updates available"
        else:
            updates_list = self.updates.split("\n")
            self.text = str(len(updates_list))
            tooltip_lines = [line.replace("\t", " ") for line in updates_list if ".." not in line]
            self.tooltip = "\n".join(tooltip_lines)

    def get_output(self):
        """Return the result in JSON format."""
        return json.dumps({
            "text": self.text,
            "tooltip": self.tooltip
        })

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--action", help="Specify the update action (pacman, yay, pikaur, trizen, flatpak)", required=True)
    args = parser.parse_args()

    control = BrightnessControl(args.action)
    control.check_updates()
    control.parse_updates()
    print(control.get_output())

if __name__ == "__main__":
    main()
