#!/usr/bin/python
import subprocess as sp


def swww(wallpaper: str, user: str) -> None:
    swww_sh = [
        "#!/usr/bin/bash",
        f"swww img {wallpaper} --transition-type center --transition-fps 60 --transition-duration 3",
    ]

    with open(
        f"/home/{user}/.config/theme-manager/run/swww.sh", "w", encoding="UTF-8"
    ) as file:
        file.writelines("\n".join(swww_sh))

    sp.run(f"bash /home/{user}/.config/theme-manager/run/swww.sh", shell=True)
