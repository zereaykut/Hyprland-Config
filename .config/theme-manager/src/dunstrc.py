#!/usr/bin/python
import subprocess as sp

def dunstrc(color_config, user):
    dunsrc_config = [
        "[global] ",
        "   ### Display ### ",
        "   monitor = 0 ",
        "   follow = mouse  ",

        "   ### Geometry ### ",
        "   width = 300 ",
        "   height = 300 ",
        "   origin = top-right ",
        "   offset = 15x49 ",
        "   scale = 0 ",
        "   notification_limit = 0  ",

        "   ### Progress bar ### ",
        "   progress_bar = true ",
        "   progress_bar_height = 10 ",
        "   progress_bar_frame_width = 1 ",
        "   progress_bar_min_width = 150 ",
        "   progress_bar_max_width = 300 ",
        "   indicate_hidden = yes ",
        "   transparency = 20 ",
        "   separator_height = 2 ",
        "   padding = 6 ",
        "   horizontal_padding = 6 ",
        "   text_icon_padding = 0 ",
        "   frame_width = 2 ",
    """     frame_color = "#aaaaaa" """,
        "   separator_color = frame ",
        "   sort = no ",
        "   idle_threshold = 0  ",

        "   ### Text ### ",
        "   font = JetBrains Mono Medium 10 ",
        "   line_height = 3 ",
        "   markup = full ",
    """     format = "<b>%s</b> %b" """,
        "   alignment = left ",
        "   vertical_alignment = center ",
        "   show_age_threshold = -1 ",
        "   ellipsize = middle ",
        "   ignore_newline = no ",
        "   stack_duplicates = true ",
        "   hide_duplicate_count = true ",
        "   show_indicators = no ",
        "   word_wrap = yes  ",

        "   ### Icons ### ",
        "   icon_position = left ",
        "   min_icon_size = 32 ",
        "   max_icon_size = 64 ",
        "   icon_path = /usr/share/icons/Paper/16x16/mimetypes/:/usr/share/icons/Paper/48x48/status/:/usr/share/icons/Paper/16x16/devices/:/usr/share/icons/Paper/48x48/notifications/:/usr/share/icons/Paper/48x48/emblems/:/usr/share/icons/gnome/16x16/status/:/usr/share/icons/gnome/16x16/devices/  ",

        "   ### History ### ",
        "   sticky_history = yes ",
        "   history_length = 30  ",

        "   ### Misc/Advanced ### ",
        "   browser = /usr/bin/xdg-open ",
        "   always_run_script = true ",
        "   title = Dunst  ",

        "   class = Dunst  ",

        "   corner_radius = 5 ",
        "   ignore_dbusclose = false  ",

        "   ### Wayland ### ",
        "   force_xwayland = false  ",

        "   ### Legacy ",
        "   force_xinerama = false  ",

        "   ### mouse ",
        "   mouse_left_click = close_current ",
        "   mouse_middle_click = do_action, close_current ",
        "   mouse_right_click = close_all  ",

        "[experimental] ",
        "   per_monitor_dpi = false  ",

        "[urgency_critical] ",
        f"""    background = "#f5e0dc" """,
        f"""    foreground = "#1e1e2e" """,
        f"""    frame_color = "#f53c3c" """,
         """    icon = "~/.config/dunst/icons/status/critical.svg" """,
           "    timeout = 8  ",

        "[urgency_low] ",
        f"""    background = "{color_config["main-bg"]}" """,
        f"""    foreground = "{color_config["main-fg"]}" """,
        f"""    frame_color = "{color_config["wb-hvr-bg"]}" """,
         """    icon = "~/.config/dunst/icons/status/arch.svg" """,
          "     timeout = 8  ",

        "[urgency_normal] ",
        f"""    background = "{color_config["main-bg"]}" """,
        f"""    foreground = "{color_config["main-fg"]}" """,
        f"""    frame_color = "{color_config["wb-hvr-bg"]}" """,
         """    icon = "~/.config/dunst/icons/status/arch.svg" """,
           "    timeout = 8 "
        ]

    with open(f"/home/{user}/.config/dunst/dunstrc", "w", encoding="UTF-8") as file:
            file.writelines("\n".join(dunsrc_config))
    
    sp.run(f"bash /home/{user}/.config/theme-manager/run/dunst.sh", shell=True)
