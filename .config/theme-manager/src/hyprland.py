#!/usr/bin/python
import subprocess as sp

def hyprland(config, color_config, theme, user):
    hyprland_theme = [
        f"""env = HYPRCURSOR_THEME,{config["cursor-theme"]}""",
        "env = HYPRCURSOR_SIZE,24",
        f"""env = XCURSOR_THEME,{config["cursor-theme"]}""",
        "env = XCURSOR_SIZE,24",
        f"""exec-once = hyprctl setcursor {config["cursor-theme"]} 24""",
        f"""exec-once = gsettings set org.gnome.desktop.interface cursor-theme '{config["cursor-theme"]}'""",
        "exec-once = gsettings set org.gnome.desktop.interface cursor-size 24",
        f"""exec-once = gsettings set org.gnome.desktop.interface icon-theme '{config["icon-theme"]}'""",
        f"exec-once = gsettings set org.gnome.desktop.interface gtk-theme '{theme}'",
        "exec-once = gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'",
        f"source = ~/.config/hypr/themes/{theme}.conf",
        "general {",
        f"""    col.active_border = rgba({color_config["wb-hvr-bg"].replace("#", "")}ff) rgba({color_config["main-fg"].replace("#", "")}ff) 45deg""",
        f"""    col.inactive_border = rgba({color_config["main-bg"].replace("#", "")}ff) rgba({color_config["wb-hvr-fg"].replace("#", "")}ff) 45deg""",
        "}",
        "group {",
        f"""    col.border_active = rgba({color_config["wb-hvr-bg"].replace("#", "")}ff) rgba({color_config["main-fg"].replace("#", "")}ff) 45deg""",
        f"""    col.border_inactive = rgba({color_config["main-bg"].replace("#", "")}ff) rgba({color_config["wb-hvr-fg"].replace("#", "")}ff) 45deg""",
        f"""    col.border_locked_active = rgba({color_config["wb-hvr-bg"].replace("#", "")}ff) rgba({color_config["main-fg"].replace("#", "")}ff) 45deg""",
        f"""    col.border_locked_inactive = rgba({color_config["main-bg"].replace("#", "")}ff) rgba({color_config["wb-hvr-fg"].replace("#", "")}ff) 45deg""",
        "}"
    ]

    hyprland_sh = [
        "#!/usr/bin/bash",
        f"""hyprctl setcursor {config["cursor-theme"]} 24""",
        "hyprctl reload"
    ]

    with open(f"/home/{user}/.config/hypr/confs/theme.conf", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(hyprland_theme))

    with open(f"/home/{user}/.config/theme-manager/run/hyprland.sh", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(hyprland_sh))

    sp.run(f"bash /home/{user}/.config/theme-manager/run/hyprland.sh", shell=True)
