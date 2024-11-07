#!/usr/bin/python


def hyprlock(theme: str, home: str) -> None:
    with open(f"{home}/.config/theme-manager/conf/hyprlock.conf", "r", encoding="UTF-8") as f:
        hyprlock_config = f.read()

    hyprlock_config = hyprlock_config.replace("""{{theme}}""", theme)

    with open(f"{home}/.config/hypr/hyprlock.conf", "w", encoding="UTF-8") as file:
        file.write(hyprlock_config)

