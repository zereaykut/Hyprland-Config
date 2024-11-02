#!/usr/bin/python
import sys
import subprocess as sp

class ClipManager:
    def __init__(self):
        self.user = sp.run("whoami", shell=True, capture_output=True, text=True).stdout.strip()

    def mode(self):
        modes = ["History", "Favorites", "Delete", "Clear History", "Exit"]
        return sp.run( f"""echo "{"\n".join(modes)}" | rofi -dmenu -matching normal -i""", shell=True, capture_output=True, text=True).stdout.strip()

    def notify(self, message: str, icon: str, timeout: int = 800) -> None:
        sp.run(
            f"""notify-send "{message}" -i {icon} -r 92999 -t {timeout} -u normal""",
            shell=True,
        )


    def history(self):
        output = sp.run("cliphist list | rofi -dmenu | cliphist decode | wl-copy", shell=True, capture_output=True, text=True).stdout
        self.notify(
            output,
            f"/home/{self.user}/.config/dunst/icons/status/clip.svg",
            800
        )

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



def main():
    # while True:
    cliphist_list = sp.run("cliphist list", shell=True, capture_output=True, text=True).stdout#.splitlines()
    # cliphist_list = [val + "\n" for val in cliphist_list]
    # print(cliphist_list)
    cmd = [
        "rofi", "-i", "-dmenu", "-kb-custom-1", "Control-Delete", 
        "-kb-custom-2", "Alt-Delete",
        "-config", "~/.config/rofi/config.rasi",
        ]
    print(cmd)
    output = sp.run(f"""rofi -i -dmenu -kb-custom-1 "Control-Delete" -kb-custom-2 "Alt-Delete" -config ~/.config/rofi/config.rasi""", shell=True, capture_output=True, text=True, check=False).stdout
    # output = sp.run(cmd, capture_output=True, check=False).stdout
    # output = sp.check_output(cmd)
    print(output)

if __name__ == "__main__":
    # main()
    clip_manager = ClipManager()
    print(clip_manager.mode())