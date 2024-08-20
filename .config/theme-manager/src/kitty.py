#!/usr/bin/python

def kitty(theme, user):
    with open(f"/home/{user}/.config/kitty/themes/theme.conf", "w", encoding="UTF-8") as file:
        file.write(f"""include /home/{user}/.config/kitty/themes/{theme}.conf""")

