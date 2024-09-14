#!/usr/bin/python
import subprocess as sp

def flatpak(config, theme, user):
    flatpak_config = [
        """#!/usr/bin/bash""",
        f"""flatpak --user override --env=GTK_THEME="{theme}" """,
        f"""flatpak --user override --env=ICON_THEME="{config["icon-theme"]}" """
        ]

    with open(f"/home/{user}/.config/theme-manager/run/flatpak.sh", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(flatpak_config))
    
    sp.run(f"bash /home/{user}/.config/theme-manager/run/flatpak.sh", shell=True)
