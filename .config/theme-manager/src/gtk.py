#!/usr/bin/python
import subprocess as sp

def gtk2(config, theme, user):
    gtk2_config = [
        f"""include "/home/{user}/.gtkrc-2.0.mine" """,
        f"""gtk-theme-name="{theme}" """,
        f"""gtk-icon-theme-name="{config["icon-theme"]}" """,
        """gtk-font-name="Cantarell 11" """,
        f"""gtk-cursor-theme-name="{config["cursor-theme"]}" """,
        "gtk-cursor-theme-size=24",
        "gtk-toolbar-style=GTK_TOOLBAR_ICONS",
        "gtk-toolbar-icon-size=GTK_ICON_SIZE_LARGE_TOOLBAR",
        "gtk-button-images=0",
        "gtk-menu-images=0",
        "gtk-enable-event-sounds=1",
        "gtk-enable-input-feedback-sounds=0",
        "gtk-xft-antialias=1",
        "gtk-xft-hinting=1",
        """gtk-xft-hintstyle="hintslight" """,
        """gtk-xft-rgba="rgb" """,
    ]
    
    with open(f"/home/{user}/.gtkrc-2.0", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(gtk2_config))

def gtk3(config, theme, user):
    gtk3_config = [
        "[Settings]",
        f"gtk-theme-name={theme}",
        f"""gtk-icon-theme-name={config["icon-theme"]}""",
        "gtk-font-name=Cantarell 11",
        f"""gtk-cursor-theme-name={config["cursor-theme"]}""",
        "gtk-cursor-theme-size=24",
        "gtk-toolbar-style=GTK_TOOLBAR_ICONS",
        "gtk-toolbar-icon-size=GTK_ICON_SIZE_LARGE_TOOLBAR",
        "gtk-button-images=0",
        "gtk-menu-images=0",
        "gtk-enable-event-sounds=1",
        "gtk-enable-input-feedback-sounds=0",
        "gtk-xft-antialias=1",
        "gtk-xft-hinting=1",
        "gtk-xft-hintstyle=hintslight",
        "gtk-xft-rgba=rgb",
        "gtk-application-prefer-dark-theme=1"
    ]

    with open(f"/home/{user}/.config/gtk-3.0/settings.ini", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(gtk3_config))

def gsettings(config, theme, user):
    gsettings_sh = [
        "#!/usr/bin/bash",
        f"""gsettings set org.gnome.desktop.interface cursor-theme '{config["cursor-theme"]}'""",
        """gsettings set org.gnome.desktop.interface cursor-size 24""",
        f"""gsettings set org.gnome.desktop.interface icon-theme '{config["icon-theme"]}'""",
        f"""gsettings set org.gnome.desktop.interface gtk-theme '{theme}'""",
        f"""gsettings set org.gnome.desktop.interface color-scheme '{config["color-scheme"]}'"""
    ]

    with open(f"/home/{user}/.config/theme-manager/run/gsettings.sh", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(gsettings_sh))

    sp.run(f"bash /home/{user}/.config/theme-manager/run/gsettings.sh", shell=True)

def default_icons(config, user):
    def_icons_config = [
        """[Icon Theme]""",
        """Name=Default""",
        """Comment=Default Cursor Theme""",
        f"""Inherits={config["cursor-theme"]}"""
    ]

    with open(f"/home/{user}/.icons/default/index.theme", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(def_icons_config))

