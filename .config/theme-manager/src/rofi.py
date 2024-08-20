#!/usr/bin/python

def rofi(color_config, user):
    rofi_theme = [
        """* {""",
        f"""    main-bg:            {color_config["main-bg"]};""",
        f"""    main-fg:            {color_config["main-fg"]};""",
        f"""    main-br:            {color_config["wb-hvr-bg"]};""",
        f"""    main-ex:            {color_config["wb-act-bg"]};""",
        f"""    select-bg:          {color_config["wb-act-bg"]};""",
        f"""    select-fg:          {color_config["wb-hvr-fg"]};""",
         """    separatorcolor:     transparent;""",
         """    border-color:       transparent;""",
        "}"
        ]

    with open(f"/home/{user}/.config/rofi/theme.rasi", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(rofi_theme))

