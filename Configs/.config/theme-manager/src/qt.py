#!/usr/bin/python


def qt5ct(config: dict, theme: str, color_config: dict, color_count: int, home: str) -> None:
    with open(f"{home}/.config/theme-manager/templates/qt5ct_colors.conf", "r", encoding="UTF-8") as f:
        qt5ct_colors = f.read()

    for i in range(color_count):
        qt5ct_colors = qt5ct_colors.replace(f"[[color{i}]]", color_config[f"color{i}"])

    with open(f"{home}/.config/qt5ct/colors.conf", "w", encoding="UTF-8") as file:
        file.write(qt5ct_colors)


    with open(f"{home}/.config/theme-manager/templates/qt5ct.conf", "r", encoding="UTF-8") as f:
        qt5ct_config = f.read()

    qt5ct_config = qt5ct_config.replace("""[[theme]]""", theme)
    qt5ct_config = qt5ct_config.replace("""[[icon-theme]]""", config["icon-theme"])

    with open(f"{home}/.config/qt5ct/qt5ct.conf", "w", encoding="UTF-8") as file:
        file.write(qt5ct_config)


def qt6ct(config: dict, theme: str, color_config: dict, color_count: int, home: str) -> None:
    with open(f"{home}/.config/theme-manager/templates/qt6ct_colors.conf", "r", encoding="UTF-8") as f:
        qt6ct_colors = f.read()

    for i in range(color_count):
        qt6ct_colors = qt6ct_colors.replace(f"[[color{i}]]", color_config[f"color{i}"])

    with open(f"{home}/.config/qt6ct/colors.conf", "w", encoding="UTF-8") as file:
        file.write(qt6ct_colors)

    with open(f"{home}/.config/theme-manager/templates/qt6ct.conf", "r", encoding="UTF-8") as f:
        qt6ct_config = f.read()

    qt6ct_config = qt6ct_config.replace("""[[theme]]""", theme)
    qt6ct_config = qt6ct_config.replace("""[[icon-theme]]""", config["icon-theme"])

    with open(f"{home}/.config/qt6ct/qt6ct.conf", "w", encoding="UTF-8") as file:
        file.write(qt6ct_config)
