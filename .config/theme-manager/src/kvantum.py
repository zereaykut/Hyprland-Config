#!/usr/bin/python

def kvantum(theme, user):
    with open(f"/home/{user}/.config/theme-manager/conf/kvantum.kvconfig", "r", encoding="UTF-8") as f:
        kvantum_kvconfig = f.read()

    kvantum_kvconfig = kvantum_kvconfig.replace("""{{theme}}""", theme)
    
    with open(f"/home/{user}/.config/Kvantum/kvantum.kvconfig", "w", encoding="UTF-8") as file:
        file.write(kvantum_kvconfig)

