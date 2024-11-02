#!/usr/bin/python
import argparse
import sys
import subprocess as sp

class ClipManager:
    def __init__(self):
        self.user = sp.run("whoami", shell=True, capture_output=True, text=True).stdout.strip()

    def mode(self):
        return sp.run("""cliphist list | rofi -i -dmenu -kb-custom-1 "Control-Delete" -kb-custom-2 "Alt-Delete" """, shell=True, capture_output=True, text=True)

    def notify(self, message: str, icon: str, timeout: int = 800) -> None:
        sp.run(f"""notify-send "{message}" -i {icon} -r 92999 -t {timeout} -u normal""", shell=True)

    def run(self):
        output = self.mode()
        returncode = output.returncode
        stdout = output.stdout
        print(returncode)
        print(stdout)
        if returncode == 10:
            # CTRL-Delete: 10
            print("Delete")
            sp.run(f'cliphist delete <<<"{stdout}"', shell=True)
            self.notify(stdout, f"/home/{self.user}/.config/dunst/icons/status/clip-edit.svg", 1000)
        elif returncode == 11:
            # ALT-Delete: 11
            print("Clear")
            sp.run("cliphist wipe", shell=True)
            self.notify("Clipbboard History Cleared", f"/home/{self.user}/.config/dunst/icons/status/clip-edit.svg", 1000)
        elif returncode == 0:
            # Enter or Selection: 0
            print("Select")
            stdout = stdout.split("\t", 1)[1].strip()
            sp.run(f'wl-copy "{stdout}"', shell=True)
            self.notify(stdout, f"/home/{self.user}/.config/dunst/icons/status/clip.svg", 1000)

            

if __name__ == "__main__":
    # main()
    clip_manager = ClipManager()
    # print(clip_manager.mode())
    clip_manager.run()