#!/usr/bin/python
import subprocess as sp


class PowerProfileManager:
    def __init__(self):
        self.power_profiles_info = {
            "Performance": "performance",
            "Balanced": "balanced",
            "Power-Saver": "power-saver"
        }
        self.power_profiles = "\n".join(list(self.power_profiles_info.keys()))

    def get_rofi_selection(self):
        rofi_select = sp.run(
            f"""echo "{self.power_profiles}" | rofi -dmenu -matching normal -i""",
            shell=True,
            capture_output=True,
            text=True,
        )
        return rofi_select.stdout.strip()

    def set_power_profile(self, profile_name):
        power_profile = self.power_profiles_info.get(profile_name)
        if power_profile:
            sp.run(f"""powerprofilesctl set {power_profile}""", shell=True)
        else:
            print(f"Invalid profile selected: {profile_name}")

    def run(self):
        selected_profile = self.get_rofi_selection()
        self.set_power_profile(selected_profile)


if __name__ == "__main__":
    manager = PowerProfileManager()
    manager.run()
