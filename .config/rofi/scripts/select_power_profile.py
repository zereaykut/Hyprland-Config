#!/usr/bin/python
import subprocess as sp

power_profiles_info = {
    "Performance": "performance",
    "Balanced": "balanced",
    "Power-Saver": "power-saver"
    }

# Power profile options for powerprofilesctl
power_profiles = "\n".join(list(power_profiles_info.keys()))

# Send created string to rofi and get selected rofi output
rofi_select = sp.run(
    f"""echo "{power_profiles}" | rofi -dmenu -matching normal -i""",
    shell=True,
    capture_output=True,
    text=True,
)

rofi_selected = rofi_select.stdout.strip()

power_profile = power_profiles_info[rofi_selected]

# Address hyprland client focus to that adderess(address of the rofi selected window)
sp.run(f"""powerprofilesctl set {power_profile}""", shell=True)
