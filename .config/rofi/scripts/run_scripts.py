#!/usr/bin/python
import subprocess as sp


class RofiScripts:
    def __init__(self):
        self.user = sp.run("whoami", shell=True, capture_output=True, text=True).stdout.strip()
        with open(f"/home/{self.user}/.config/rofi/scripts/run_scripts.json", "r") as f:
            self.rofi_scripts_info = json.load(f)
        self.rofi_scripts = "\n".join(list(self.rofi_scripts_info.keys()))

    def get_rofi_selection(self):
        rofi_select = sp.run(
            f"""echo "{self.rofi_scripts}" | rofi -dmenu -matching normal -i""",
            shell=True,
            capture_output=True,
            text=True,
        )
        return rofi_select.stdout.strip()

    def run_script(self, script_name):
        run_script = self.rofi_scripts_info.get(script_name)
        if run_script:
            sp.run(run_script, shell=True)
        else:
            print(f"Invalid profile selected: {script_name}")

    def run(self):
        script_name = self.get_rofi_selection()
        self.run_script(script_name)


if __name__ == "__main__":
    manager = RofiScripts()
    manager.run()
