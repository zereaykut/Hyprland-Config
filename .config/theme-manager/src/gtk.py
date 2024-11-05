#!/usr/bin/python
import subprocess as sp


def gtk2(config: dict, theme: str, cursor_size: int, user: str) -> None:
    with open(
        f"/home/{user}/.config/theme-manager/conf/gtk2", "r", encoding="UTF-8"
    ) as f:
        gtk2_config = f.read()

    gtk2_config = gtk2_config.replace("""{{user}}""", user)
    gtk2_config = gtk2_config.replace("""{{theme}}""", theme)
    gtk2_config = gtk2_config.replace("""{{icon-theme}}""", config["icon-theme"])
    gtk2_config = gtk2_config.replace("""{{cursor-theme}}""", config["cursor-theme"])
    gtk2_config = gtk2_config.replace("""{{cursor-size}}""", str(cursor_size))

    with open(f"/home/{user}/.gtkrc-2.0", "w", encoding="UTF-8") as file:
        file.write(gtk2_config)


def gtk3(config: dict, theme: str, cursor_size: int, user: str) -> None:
    with open(
        f"/home/{user}/.config/theme-manager/conf/gtk3", "r", encoding="UTF-8"
    ) as f:
        gtk3_config = f.read()

    gtk3_config = gtk3_config.replace("""{{theme}}""", theme)
    gtk3_config = gtk3_config.replace("""{{icon-theme}}""", config["icon-theme"])
    gtk3_config = gtk3_config.replace("""{{cursor-theme}}""", config["cursor-theme"])
    gtk3_config = gtk3_config.replace("""{{cursor-size}}""", str(cursor_size))

    with open(
        f"/home/{user}/.config/gtk-3.0/settings.ini", "w", encoding="UTF-8"
    ) as file:
        file.write(gtk3_config)


def gsettings(config: dict, theme: str, user: str, cursor_size: int) -> None:
    sp.run(["gsettings", "set", "org.gnome.desktop.interface", "cursor-theme", f"'{config["cursor-theme"]}'"])
    sp.run(["gsettings", "set", "org.gnome.desktop.interface", "cursor-size", str(cursor_size)])
    sp.run(["gsettings", "set", "org.gnome.desktop.interface", "icon-theme", f"'{config["icon-theme"]}'"])
    sp.run(["gsettings", "set", "org.gnome.desktop.interface", "gtk-theme", f"'{theme}'"])
    sp.run(["gsettings", "set", "org.gnome.desktop.interface", "color-scheme", f"'{config["color-scheme"]}'"])


def default_icons(config: dict, user: str) -> None:
    with open(
        f"/home/{user}/.config/theme-manager/conf/gtk_def_index", "r", encoding="UTF-8"
    ) as f:
        gtk_def_index = f.read()

    gtk_def_index = gtk_def_index.replace(
        """{{cursor-theme}}""", config["cursor-theme"]
    )

    with open(
        f"/home/{user}/.icons/default/index.theme", "w", encoding="UTF-8"
    ) as file:
        file.write(gtk_def_index)
