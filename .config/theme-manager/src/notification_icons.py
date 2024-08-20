#!/usr/bin/python
import subprocess as sp

def mic_unmuted(color_config, user):
    data = [
        """<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">""",
        """<!-- Uploaded to: SVG Repo, www.svgrepo.com, Transformed by: SVG Repo Mixer Tools -->""",
        """<svg width="120px" height="120px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">""",
        """<g id="SVGRepo_bgCarrier" stroke-width="0"/>""",
        """<g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>""",
        """<g id="SVGRepo_iconCarrier"> <path opacity="0.15" d="M9 6C9 4.34315 10.3431 3 12 3C13.6569 3 15 4.34315 15 6V12C15 13.6569 13.6569 15 12 15C10.3431 15 9 13.6569 9 12V6Z" fill="#000000" style="--darkreader-inline-fill: #000000;" data-darkreader-inline-fill=""/> """,
        """<path d="M18 12C18 15.3137 15.3137 18 12 18M12 18C8.68629 18 6 15.3137 6 12M12 18V21M12 21H15M12 21H9M15 6V12C15 13.6569 13.6569 15 12 15C10.3431 15 9 13.6569 9 12V6C9 4.34315 10.3431 3 12 3C13.6569 3 15 4.34315 15 6Z" """,
        f"""stroke="{color_config["wb-hvr-bg"]}" """,
        """    stroke-width="1.5" """,
        """    stroke-linecap="round" """,
        """    stroke-linejoin="round" """,
        """    style="--darkreader-inline-stroke: #ffffff;" """,
        """    data-darkreader-inline-stroke=""/> </g>""",
        "</svg>"
        ]

    with open(f"/home/{user}/.config/dunst/icons/status/mic-unmuted.svg", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(data))

def mic_muted(color_config, user):
    data = [
        """<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">""",
        """<!-- Uploaded to: SVG Repo, www.svgrepo.com, Transformed by: SVG Repo Mixer Tools -->""",
        """<svg width="120px" height="120px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">""",
        """<g id="SVGRepo_bgCarrier" stroke-width="0"/>""",
        """<g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>""",
        "<g ",
        """    id="SVGRepo_iconCarrier"> <path d="M9.40137 4.5C9.92008 3.6033 10.8896 3 12 3C13.6569 3 15 4.34315 15 6V10M18 12C18 12.3407 17.9716 12.6748 17.9171 13M3 3L21 21M12 18C8.68629 18 6 15.3137 6 12M12 18C12.3407 18 12.6748 17.9716 13 17.917M12 18V21M12 21H15M12 21H9" """,
        f"""stroke="{color_config["wb-hvr-bg"]}" """,
        """    stroke-width="1.5" """,
        """    stroke-linecap="round" """,
        """    stroke-linejoin="round" """,
        """    style="--darkreader-inline-stroke: #ffffff;" """,
        """    data-darkreader-inline-stroke=""/> </g>""",
        "</svg>"
        ]

    with open(f"/home/{user}/.config/dunst/icons/status/mic-muted.svg", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(data))

def speaker_unmuted(color_config, user):
    data = [
        """<?xml version="1.0" encoding="utf-8"?><!-- Uploaded to: SVG Repo, www.svgrepo.com, Generator: SVG Repo Mixer Tools -->""",
        "<svg ",
        f"""fill="{color_config["wb-hvr-bg"]}" """,
        """    width="120px" """,
        """    height="120px" """,
        """    viewBox="0 0 56 56" """,
        """    xmlns="http://www.w3.org/2000/svg">""",
        """<path d="M 39.7305 49.5039 C 41.3242 49.5039 42.4726 48.3320 42.4726 46.7617 L 42.4726 9.3789 C 42.4726 7.8086 41.3242 6.4961 39.6836 6.4961 C 38.5352 6.4961 37.7617 7.0117 36.5195 8.1836 L 26.1836 17.9570 C 26.0195 18.0977 25.8086 18.1680 25.5742 18.1680 L 18.6133 18.1680 C 15.3086 18.1680 13.5274 19.9726 13.5274 23.4883 L 13.5274 32.5820 C 13.5274 36.0977 15.3086 37.9024 18.6133 37.9024 L 25.5742 37.9024 C 25.8086 37.9024 26.0195 37.9726 26.1836 38.1133 L 36.5195 47.9805 C 37.6445 49.0352 38.5820 49.5039 39.7305 49.5039 Z"/></svg>"""
        ]

    with open(f"/home/{user}/.config/dunst/icons/status/speaker-unmuted.svg", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(data))

def speaker_muted(color_config, user):
    data = [
        """<?xml version="1.0" encoding="utf-8"?><!-- Uploaded to: SVG Repo, www.svgrepo.com, Generator: SVG Repo Mixer Tools -->""",
        "<svg ",
        f"""fill="{color_config["wb-hvr-bg"]}" """,
        """    width="120px" """,
        """    height="120px" """,
        """    viewBox="0 0 56 56" """,
        """    xmlns="http://www.w3.org/2000/svg">""",
        """<path d="M 39.1796 33.4024 L 39.1796 8.2070 C 39.1796 6.6367 38.0312 5.3242 36.3906 5.3242 C 35.2421 5.3242 34.4687 5.8398 33.2265 7.0117 L 23.6171 16.1055 C 23.4765 16.2461 23.3359 16.3398 23.1718 16.3867 L 22.2343 16.4570 Z M 46.7733 49.9727 C 47.4999 50.6758 48.6484 50.6758 49.3280 49.9727 C 50.0312 49.2461 50.0548 48.1211 49.3280 47.4180 L 9.2030 7.2929 C 8.4999 6.5898 7.3280 6.5898 6.6249 7.2929 C 5.9452 7.9727 5.9452 9.1680 6.6249 9.8476 Z M 36.4374 48.3320 C 37.8202 48.3320 38.7812 47.5117 39.0859 46.1289 L 11.4062 18.4961 C 10.6562 19.3867 10.2343 20.6758 10.2343 22.3164 L 10.2343 31.4102 C 10.2343 34.9258 12.0155 36.7305 15.3202 36.7305 L 22.2812 36.7305 C 22.5155 36.7305 22.7265 36.8008 22.8671 36.9414 L 33.2265 46.8086 C 34.3515 47.8633 35.2890 48.3320 36.4374 48.3320 Z"/></svg>"""
        ]

    with open(f"/home/{user}/.config/dunst/icons/status/speaker-muted.svg", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(data))

def lock_unlocked(color_config, user):
    data = [
        """<?xml version="1.0" encoding="utf-8"?><!-- Uploaded to: SVG Repo, www.svgrepo.com, Generator: SVG Repo Mixer Tools -->""",
        """<svg width="800px" height="800px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">""",
        """<path d="M3 3L21 21M17 10V8C17 5.23858 14.7614 3 12 3C11.0283 3 10.1213 3.27719 9.35386 3.75681M7.08383 7.08338C7.02878 7.38053 7 7.6869 7 8V10.0288M19.5614 19.5618C19.273 20.0348 18.8583 20.4201 18.362 20.673C17.7202 21 16.8802 21 15.2 21H8.8C7.11984 21 6.27976 21 5.63803 20.673C5.07354 20.3854 4.6146 19.9265 4.32698 19.362C4 18.7202 4 17.8802 4 16.2V14.8C4 13.1198 4 12.2798 4.32698 11.638C4.6146 11.0735 5.07354 10.6146 5.63803 10.327C5.99429 10.1455 6.41168 10.0647 7 10.0288M19.9998 14.4023C19.9978 12.9831 19.9731 12.227 19.673 11.638C19.3854 11.0735 18.9265 10.6146 18.362 10.327C17.773 10.0269 17.0169 10.0022 15.5977 10.0002M10 10H8.8C8.05259 10 7.47142 10 7 10.0288" """,
        f"""stroke="{color_config["wb-hvr-bg"]}" """,
        """    stroke-width="2" """,
        """    stroke-linecap="round" """,
        """    stroke-linejoin="round"/>""",
        "</svg>"
        ]

    with open(f"/home/{user}/.config/dunst/icons/status/lock-unlocked.svg", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(data))

def lock_locked(color_config, user):
    data = [
        """<?xml version="1.0" encoding="utf-8"?><!-- Uploaded to: SVG Repo, www.svgrepo.com, Generator: SVG Repo Mixer Tools -->""",
        """<svg width="800px" height="800px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">""",
        """<path d="M7 10.0288C7.47142 10 8.05259 10 8.8 10H15.2C15.9474 10 16.5286 10 17 10.0288M7 10.0288C6.41168 10.0647 5.99429 10.1455 5.63803 10.327C5.07354 10.6146 4.6146 11.0735 4.32698 11.638C4 12.2798 4 13.1198 4 14.8V16.2C4 17.8802 4 18.7202 4.32698 19.362C4.6146 19.9265 5.07354 20.3854 5.63803 20.673C6.27976 21 7.11984 21 8.8 21H15.2C16.8802 21 17.7202 21 18.362 20.673C18.9265 20.3854 19.3854 19.9265 19.673 19.362C20 18.7202 20 17.8802 20 16.2V14.8C20 13.1198 20 12.2798 19.673 11.638C19.3854 11.0735 18.9265 10.6146 18.362 10.327C18.0057 10.1455 17.5883 10.0647 17 10.0288M7 10.0288V8C7 5.23858 9.23858 3 12 3C14.7614 3 17 5.23858 17 8V10.0288" """,
        f"""stroke="{color_config["wb-hvr-bg"]}" """,
        """    stroke-width="2" """,
        """    stroke-linecap="round" """,
        """    stroke-linejoin="round"/>""",
        "</svg>"
        ]

    with open(f"/home/{user}/.config/dunst/icons/status/lock-locked.svg", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(data))

def wifi_enabled(color_config, user):
    data = [
        """<?xml version="1.0" encoding="utf-8"?><!-- Uploaded to: SVG Repo, www.svgrepo.com, Generator: SVG Repo Mixer Tools -->""",
        """<svg width="800px" height="800px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">""",
        """<path d="M1.33309 8.07433C0.92156 8.44266 0.886539 9.07485 1.25487 9.48638C1.62319 9.89791 2.25539 9.93293 2.66691 9.5646L1.33309 8.07433ZM21.3331 9.5646C21.7446 9.93293 22.3768 9.89791 22.7451 9.48638C23.1135 9.07485 23.0784 8.44266 22.6669 8.07433L21.3331 9.5646ZM12 19C11.4477 19 11 19.4477 11 20C11 20.5523 11.4477 21 12 21V19ZM12.01 21C12.5623 21 13.01 20.5523 13.01 20C13.01 19.4477 12.5623 19 12.01 19V21ZM14.6905 17.04C15.099 17.4116 15.7315 17.3817 16.1031 16.9732C16.4748 16.5646 16.4448 15.9322 16.0363 15.5605L14.6905 17.04ZM18.0539 13.3403C18.4624 13.7119 19.0949 13.682 19.4665 13.2734C19.8381 12.8649 19.8082 12.2324 19.3997 11.8608L18.0539 13.3403ZM7.96372 15.5605C7.55517 15.9322 7.52524 16.5646 7.89687 16.9732C8.2685 17.3817 8.90095 17.4116 9.3095 17.04L7.96372 15.5605ZM4.60034 11.8608C4.19179 12.2324 4.16185 12.8649 4.53348 13.2734C4.90511 13.682 5.53756 13.7119 5.94611 13.3403L4.60034 11.8608ZM2.66691 9.5646C5.14444 7.34716 8.41371 6 12 6V4C7.90275 4 4.16312 5.54138 1.33309 8.07433L2.66691 9.5646ZM12 6C15.5863 6 18.8556 7.34716 21.3331 9.5646L22.6669 8.07433C19.8369 5.54138 16.0972 4 12 4V6ZM12 21H12.01V19H12V21ZM12 16C13.0367 16 13.9793 16.3931 14.6905 17.04L16.0363 15.5605C14.9713 14.5918 13.5536 14 12 14V16ZM12 11C14.3319 11 16.4546 11.8855 18.0539 13.3403L19.3997 11.8608C17.4466 10.0842 14.8487 9 12 9V11ZM9.3095 17.04C10.0207 16.3931 10.9633 16 12 16V14C10.4464 14 9.02872 14.5918 7.96372 15.5605L9.3095 17.04ZM5.94611 13.3403C7.54544 11.8855 9.66815 11 12 11V9C9.15127 9 6.55344 10.0842 4.60034 11.8608L5.94611 13.3403Z" """,
        f"""    fill="{color_config["wb-hvr-bg"]}" """,
        """    />""",
        """</svg>"""
        ]

    with open(f"/home/{user}/.config/dunst/icons/status/wifi-enabled.svg", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(data))

def wifi_disabled(color_config, user):
    data = [
        """<?xml version="1.0" encoding="utf-8"?><!-- Uploaded to: SVG Repo, www.svgrepo.com, Generator: SVG Repo Mixer Tools -->""",
        """<svg width="800px" height="800px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">""",
        """<path d="M1.33309 8.07433C0.92156 8.44266 0.886539 9.07485 1.25487 9.48638C1.62319 9.89791 2.25539 9.93293 2.66691 9.5646L1.33309 8.07433ZM21.3331 9.5646C21.7446 9.93293 22.3768 9.89791 22.7451 9.48638C23.1135 9.07485 23.0784 8.44266 22.6669 8.07433L21.3331 9.5646ZM12 19C11.4477 19 11 19.4477 11 20C11 20.5523 11.4477 21 12 21V19ZM12.01 21C12.5623 21 13.01 20.5523 13.01 20C13.01 19.4477 12.5623 19 12.01 19V21ZM14.6905 17.04C15.099 17.4116 15.7315 17.3817 16.1031 16.9732C16.4748 16.5646 16.4448 15.9322 16.0363 15.5605L14.6905 17.04ZM18.0539 13.3403C18.4624 13.7119 19.0949 13.682 19.4665 13.2734C19.8381 12.8649 19.8082 12.2324 19.3997 11.8608L18.0539 13.3403ZM7.96372 15.5605C7.55517 15.9322 7.52524 16.5646 7.89687 16.9732C8.2685 17.3817 8.90095 17.4116 9.3095 17.04L7.96372 15.5605ZM4.60034 11.8608C4.19179 12.2324 4.16185 12.8649 4.53348 13.2734C4.90511 13.682 5.53756 13.7119 5.94611 13.3403L4.60034 11.8608ZM10.5705 4.06305C10.0204 4.1118 9.61391 4.59729 9.66266 5.14741C9.71141 5.69754 10.1969 6.10399 10.747 6.05525L10.5705 4.06305ZM17.3393 10.3798C16.8567 10.1114 16.2478 10.285 15.9794 10.7677C15.711 11.2504 15.8847 11.8593 16.3673 12.1277L17.3393 10.3798ZM3.70711 2.29289C3.31658 1.90237 2.68342 1.90237 2.29289 2.29289C1.90237 2.68342 1.90237 3.31658 2.29289 3.70711L3.70711 2.29289ZM20.2929 21.7071C20.6834 22.0976 21.3166 22.0976 21.7071 21.7071C22.0976 21.3166 22.0976 20.6834 21.7071 20.2929L20.2929 21.7071ZM12 6C15.5863 6 18.8556 7.34716 21.3331 9.5646L22.6669 8.07433C19.8369 5.54138 16.0972 4 12 4V6ZM12 21H12.01V19H12V21ZM12 16C13.0367 16 13.9793 16.3931 14.6905 17.04L16.0363 15.5605C14.9713 14.5918 13.5536 14 12 14V16ZM9.3095 17.04C10.0207 16.3931 10.9633 16 12 16V14C10.4464 14 9.02872 14.5918 7.96372 15.5605L9.3095 17.04ZM10.747 6.05525C11.1596 6.01869 11.5775 6 12 6V4C11.5185 4 11.0417 4.0213 10.5705 4.06305L10.747 6.05525ZM16.3673 12.1277C16.9757 12.466 17.5412 12.874 18.0539 13.3403L19.3997 11.8608C18.7751 11.2927 18.0844 10.7941 17.3393 10.3798L16.3673 12.1277ZM2.29289 3.70711L5.46648 6.8807L6.8807 5.46648L3.70711 2.29289L2.29289 3.70711ZM2.66691 9.5646C3.81213 8.53961 5.12648 7.70074 6.56232 7.09494L5.78486 5.25224C4.14251 5.94517 2.64069 6.904 1.33309 8.07433L2.66691 9.5646ZM5.46648 6.8807L9.46042 10.8746L10.8746 9.46042L6.8807 5.46648L5.46648 6.8807ZM9.46042 10.8746L20.2929 21.7071L21.7071 20.2929L10.8746 9.46042L9.46042 10.8746ZM5.94611 13.3403C7.15939 12.2367 8.67355 11.4612 10.3496 11.1508L9.98543 9.18424C7.93271 9.5644 6.08108 10.5139 4.60034 11.8608L5.94611 13.3403Z" """,
        f"""    fill="{color_config["wb-hvr-bg"]}" """,
        """    />""",
        """</svg>"""
        ]
    with open(f"/home/{user}/.config/dunst/icons/status/wifi-disabled.svg", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(data))

def vol_icons(color_config, user):
    for vol in range(0, 101, 5):
        with open(f"/home/{user}/.config/theme-manager/icons/vol/vol-{vol}.svg", "r", encoding="UTF-8") as file:
            data = file.readlines()
        data[51] = f"""fill:{color_config["wb-hvr-fg"]};\n"""
        data[91] = f"""fill:{color_config["wb-hvr-bg"]};\n"""
        with open(f"/home/{user}/.config/dunst/icons/vol/vol-{vol}.svg", "w", encoding="UTF-8") as file:
            file.writelines(data)