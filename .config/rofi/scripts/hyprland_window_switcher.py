#!/usr/bin/python
import json
import subprocess as sp

# Get hyprland client infos as text and load as json(dictionary)
windows = sp.run("hyprctl clients -j", shell=True, capture_output=True, text=True)
windows = json.loads(windows.stdout)

# Create a string, that has windows infos, to send rofi

# Data Preprocess
rofi_list = []
for window in windows:
    # Add if class name is not empty
    if window["class"] != "":
        ws_ = window["workspace"]["name"]
        class_ = window["class"]
        # fix class (example: org.kde.dolphin)
        if class_[:3] == "org":
            class_ = class_.split(".")[-1]

        title_ = window["title"]
        address_ = window["address"]
        rofi_list.append(
            {"ws": ws_, "class": class_, "title": title_, "address": address_}
        )
# sort outputs according to workspace
rofi_list = sorted(rofi_list, key=lambda x: x["ws"])

rofi_output = ""
for window in rofi_list:
    if rofi_output == "":
        rofi_output = f"""ws {window.get("ws")} | {window.get("class")} <> {window.get("title")}   || {window.get("address")}"""
    else:
        rofi_output = f"""{rofi_output}\nws {window.get("ws")} | {window.get("class")} <> {window.get("title")}   || {window.get("address")}"""

# Send created string to rofi and get selected rofi output
rofi_select = sp.run(
    f"""echo "{rofi_output}" | rofi -dmenu -matching normal -i""",
    shell=True,
    capture_output=True,
    text=True,
)
rofi_select_address = rofi_select.stdout.split("||")[-1].strip()

# Address hyprland client focus to that adderess(address of the rofi selected window)
sp.run(f"""hyprctl dispatch focuswindow address:{rofi_select_address}""", shell=True)
