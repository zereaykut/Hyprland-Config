#!/usr/bin/python

def qt5ct(config, theme, user):
    qt5ct_config = [
        "[Appearance]",
        f"color_scheme_path=~/.config/qt5ct/colors/{theme}.conf",
        "custom_palette=false",
        f"""icon_theme={config["icon-theme"]}""",
        "standard_dialogs=default",
        "style=kvantum",
        "[Fonts]",
        """fixed="Sans Serif,10,-1,5,50,0,0,0,0,0" """,
        """general="Sans Serif,10,-1,5,50,0,0,0,0,0" """,
        "[Interface]",
        "activate_item_on_single_click=1",
        "buttonbox_layout=0",
        "cursor_flash_time=1000",
        "dialog_buttons_have_icons=1",
        "double_click_interval=400",
        "gui_effects=@Invalid()",
        "keyboard_scheme=2",
        "menus_have_icons=true",
        "show_shortcuts_in_context_menus=true",
        "stylesheets=@Invalid()",
        "toolbutton_style=4",
        "underline_shortcut=1",
        "wheel_scroll_lines=3",
        "[SettingsWindow]",
        r"""geometry=@ByteArray(\x1\xd9\xd0\xcb\0\x3\0\0\0\0\0\0\0\0\0\0\0\0\x3\xaa\0\0\x3\xfc\0\0\0\0\0\0\0\0\0\0\x2\xde\0\0\x2_\0\0\0\0\x2\0\0\0\a\x80\0\0\0\0\0\0\0\0\0\0\x3\xaa\0\0\x3\xfc)""",
        "[Troubleshooting]",
        "force_raster_widgets=1",
        "ignored_applications=@Invalid()"
        ]

    with open(f"/home/{user}/.config/qt5ct/qt5ct.conf", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(qt5ct_config))

def qt6ct(config, theme, user):
    qt6ct_config = [
        "[Appearance]",
        f"color_scheme_path=~/.config/qt5ct/colors/{theme}.conf",
        "custom_palette=false",
        f"""icon_theme={config["icon-theme"]}""",
        "standard_dialogs=default",
        "style=kvantum",
        "[Fonts]",
        """fixed="Sans Serif,10,-1,5,50,0,0,0,0,0" """,
        """general="Sans Serif,10,-1,5,50,0,0,0,0,0" """,
        "[Interface]",
        "activate_item_on_single_click=1",
        "buttonbox_layout=0",
        "cursor_flash_time=1000",
        "dialog_buttons_have_icons=1",
        "double_click_interval=400",
        "gui_effects=@Invalid()",
        "keyboard_scheme=2",
        "menus_have_icons=true",
        "show_shortcuts_in_context_menus=true",
        "stylesheets=@Invalid()",
        "toolbutton_style=4",
        "underline_shortcut=1",
        "wheel_scroll_lines=3",
        "[SettingsWindow]",
        r"""geometry=@ByteArray(\x1\xd9\xd0\xcb\0\x3\0\0\0\0\0\0\0\0\0\0\0\0\x3\xaa\0\0\x3\xfc\0\0\0\0\0\0\0\0\0\0\x2\xde\0\0\x2_\0\0\0\0\x2\0\0\0\a\x80\0\0\0\0\0\0\0\0\0\0\x3\xaa\0\0\x3\xfc)""",
        "[Troubleshooting]",
        "force_raster_widgets=1",
        "ignored_applications=@Invalid()",
        ]
    
    with open(f"/home/{user}/.config/qt6ct/qt6ct.conf", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(qt6ct_config))
