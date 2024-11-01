#!/usr/bin/python
import sys
import subprocess as sp

def main():
    while True:
        cmd = [
            "echo", "$(cliphist list)",
            "rofi", "-i", "-dmenu", "-kb-custom-1", '"Control-Delete"', 
            "-kb-custom-2", '"Alt-Delete"',
            "-config", "~/.config/rofi/config.rasi",
            ]
        sp.run(cmd, shell=True, capture_output=True, text=True)

if __name__ == "__main__":
    main()