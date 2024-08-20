#!/usr/bin/python

def btop(theme, user):
    with open(f"/home/{user}/.config/theme-manager/conf/btop.conf", "r", encoding="UTF-8") as f:
        btop_config = f.readlines()

    btop_config[4] = f"""color_theme = "/home/{user}/.config/btop/themes/{theme}.theme"\n"""
    
    with open(f"/home/{user}/.config/btop/btop.conf", "w", encoding="UTF-8") as file:
            file.writelines(btop_config)
