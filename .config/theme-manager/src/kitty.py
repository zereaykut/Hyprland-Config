#!/usr/bin/python

def kitty(theme, user):
    with open(f"/home/{user}/.config/theme-manager/conf/kitty.conf", "r", encoding="UTF-8") as f:
        kitty_config = f.read()

    kitty_config = kitty_config.replace("""{{theme}}""", theme)

    with open(f"/home/{user}/.config/kitty/kitty.conf", "w", encoding="UTF-8") as file:
        file.write(kitty_config)
