#!/usr/bin/python
import subprocess as sp


def sddm(
    config: dict,
    color_config: dict,
    theme: str,
    cursor_size: int,
    user: str,
    screen_width: int = 1920,
    screen_height: int = 1080,
):
    with open(
        f"/home/{user}/.config/theme-manager/conf/sddm_theme_base.conf",
        "r",
        encoding="UTF-8",
    ) as f:
        sddm_theme = f.read()

    sddm_theme = sddm_theme.replace("""{{theme}}""", theme)

    sddm_theme = sddm_theme.replace("""{{screen-width}}""", str(screen_width))
    sddm_theme = sddm_theme.replace("""{{screen-height}}""", str(screen_height))

    sddm_theme = sddm_theme.replace("""{{main-fg}}""", color_config["main-fg"])

    with open(
        f"/home/{user}/.config/theme-manager/conf/sddm_theme.conf",
        "w",
        encoding="UTF-8",
    ) as file:
        file.write(sddm_theme)

    with open(
        f"/home/{user}/.config/theme-manager/conf/sddm_base.conf", "r", encoding="UTF-8"
    ) as f:
        sddm_config = f.read()

    sddm_config = sddm_config.replace("""{{cursor-theme}}""", config["cursor-theme"])
    sddm_config = sddm_config.replace("""{{cursor-size}}""", str(cursor_size))

    with open(
        f"/home/{user}/.config/theme-manager/conf/sddm.conf", "w", encoding="UTF-8"
    ) as file:
        file.write(sddm_config)

    sp.run(["pkexec", "cp", f"/home/{user}/.config/theme-manager/conf/sddm_theme.conf", "/usr/share/sddm/themes/Simple-SDDM/theme.conf"])
    sp.run(["pkexec", "cp", f"/home/{user}/.config/theme-manager/conf/sddm.conf", "/etc/sddm.conf"])
