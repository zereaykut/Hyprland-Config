#!/usr/bin/python
import argparse
import sys
import subprocess as sp

class ClipManager:
    def __init__(self):
        self.user = sp.run("whoami", shell=True, capture_output=True, text=True).stdout.strip()
        self.modes = ["History", "Favorites", "Delete", "Clear History", "Exit"]

    def mode(self):
        return sp.run( f"""echo "{"\n".join(self.modes)}" | rofi -dmenu -matching normal -i""", shell=True, capture_output=True, text=True).stdout.strip()

    def notify(self, message: str, icon: str, timeout: int = 800) -> None:
        sp.run(
            f"""notify-send "{message}" -i {icon} -r 92999 -t {timeout} -u normal""",
            shell=True,
        )

    def history(self):
        output = sp.run("cliphist list | rofi -dmenu | cliphist decode | wl-copy", shell=True, capture_output=True, text=True).stdout
        print(output)
        self.notify(
            output,
            f"/home/{self.user}/.config/dunst/icons/status/clip.svg",
            800
        )
        sys.exit()

    def favorites(self):
        pass
    
    def delete(self):
        output = sp.run("cliphist list | rofi -dmenu | cliphist delete", shell=True, capture_output=True, text=True).stdout
        self.notify(
            output,
            f"/home/{self.user}/.config/dunst/icons/status/clip-edit.svg",
            800
        )

    def claer_history(self):
        sp.run("cliphist wipe", shell=True)
        self.notify(
            "Clipboard History Cleared",
            f"/home/{self.user}/.config/dunst/icons/status/clip-edit.svg",
            800
        )
    
    def exit(self):
        sys.exit()

    def run(self):
        # parser = argparse.ArgumentParser()
        # parser.add_argument("-a", "--mode", help="Clip manager modes among History, Favorites, Delete, Clear History, and Exit")

        # args = parser.parse_args()
        # mode_ = args.mode
        mode_ = self.mode()

        if mode_ == "History":
            self.history()
        elif mode_ == "Favorites":
            sys.exit()
        elif mode_ == "Delete":
            while True:
                self.delete()
        elif mode_ == "Clear History":
            self.claer_history()
        else:
            print("No arguments")
            sys.exit()

if __name__ == "__main__":
    # main()
    clip_manager = ClipManager()
    # print(clip_manager.mode())
    clip_manager.run()