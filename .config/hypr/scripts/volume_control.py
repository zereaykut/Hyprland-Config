#!/usr/bin/python
import argparse
import subprocess as sp
import sys

class VolumeControl:
    def __init__(self, action, device):
        self.user = sp.run("whoami", shell=True, capture_output=True, text=True).stdout.strip()
        self.action = action
        self.device = device
        self.src = self.get_device_source()

    def get_device_source(self):
        if self.device == "i":
            return "--default-source"
        elif self.device == "o":
            return ""
        else:
            sys.exit("Invalid device parameter")

    def set_volume(self):
        if self.action == "i":
            sp.run(f"pamixer {self.src} -i 5", shell=True)
        elif self.action == "d":
            sp.run(f"pamixer {self.src} -d 5", shell=True)
        elif self.action == "m":
            sp.run(f"pamixer {self.src} -t", shell=True)
        else:
            sys.exit("Invalid action parameter")

    def send_notification(self):
        if self.action == "m":
            self.notify_mute_status()
        else:
            self.notify_volume_change()

    def notify_mute_status(self):
        mute_state = sp.run(f"pamixer {self.src} --get-mute", shell=True, capture_output=True, text=True).stdout.strip()
        if mute_state == "true":
            if self.device == "o":
                icon = f"/home/{self.user}/.config/dunst/icons/status/speaker-muted.svg"
                message = "Speaker is muted"
            elif self.device == "i":
                icon = f"/home/{self.user}/.config/dunst/icons/status/mic-muted.svg"
                message = "Microphone is muted"
            else:
                sys.exit("Invalid device parameter")
        else:
            if self.device == "o":
                icon = f"/home/{self.user}/.config/dunst/icons/status/speaker-unmuted.svg"
                message = "Speaker is unmuted"
            elif self.device == "i":
                icon = f"/home/{self.user}/.config/dunst/icons/status/mic-unmuted.svg"
                message = "Microphone is unmuted"
            else:
                sys.exit("Invalid device parameter")

        sp.run(f"""dunstify "{message}" -i {icon} -r 91190 -t 800 -u normal""", shell=True)

    def notify_volume_change(self):
        volume_percent = int(sp.run(f"pamixer {self.src} --get-volume", shell=True, capture_output=True, text=True).stdout.strip())
        volume_vol = volume_percent // 5 * 5
        icon = f"/home/{self.user}/.config/dunst/icons/vol/vol-{volume_vol}.svg"
        sp.run(f"""dunstify "Volume {volume_percent}%" -i {icon} -r 91190 -t 800 -u normal""", shell=True)

def main():
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

    parser = argparse.ArgumentParser(description="Control volume and send notifications.")
    parser.add_argument("-a", "--action", help="Action to increase, decrease, or mute volume", required=True)
    parser.add_argument("-d", "--device", help="Device to apply the action (input or output)", required=True)
    
    args = parser.parse_args()
    
    volume_control = VolumeControl(args.action, args.device)
    volume_control.set_volume()
    volume_control.send_notification()

if __name__ == "__main__":
    main()
