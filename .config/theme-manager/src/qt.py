#!/usr/bin/python


def qt5ct(config: dict, theme: str, user: str) -> None:
    with open(
        f"/home/{user}/.config/theme-manager/conf/qt5ct.conf", "r", encoding="UTF-8"
    ) as f:
        qt5ct_config = f.read()

    qt5ct_config = qt5ct_config.replace("""{{theme}}""", theme)
    qt5ct_config = qt5ct_config.replace("""{{icon-theme}}""", config["icon-theme"])

    with open(f"/home/{user}/.config/qt5ct/qt5ct.conf", "w", encoding="UTF-8") as file:
        file.write(qt5ct_config)


def qt6ct(config: dict, theme: str, user: str) -> None:
    with open(
        f"/home/{user}/.config/theme-manager/conf/qt6ct.conf", "r", encoding="UTF-8"
    ) as f:
        qt6ct_config = f.read()

    qt6ct_config = qt6ct_config.replace("""{{theme}}""", theme)
    qt6ct_config = qt6ct_config.replace("""{{icon-theme}}""", config["icon-theme"])

    with open(f"/home/{user}/.config/qt6ct/qt6ct.conf", "w", encoding="UTF-8") as file:
        file.write(qt6ct_config)
