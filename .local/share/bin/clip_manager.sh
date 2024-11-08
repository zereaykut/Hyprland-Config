#!/bin/bash
# source = https://github.com/JaKooLit/Hyprland-Dots/blob/main/config/hypr/scripts/ClipManager.sh

# CTRL Del to delete an entry
# ALT Del to wipe clipboard contents

while true; do
    result=$(rofi -i -dmenu -kb-custom-1 "Control-Delete" -kb-custom-2 "Alt-Delete" -config ~/.config/rofi/rofi_selector.rasi< <(cliphist list))

    case "$?" in
        1)
            exit
            ;;
        0)
            case "$result" in
                "")
                    continue
                    ;;
                *)
                    cliphist decode <<<"$result" | wl-copy
                    notify-send "$result" -i ~/.config/dunst/icons/status/clip.svg -r 92999 -t 1000 -u normal
                    exit
                    ;;
            esac
            ;;
        10)
            echo "$result"
            cliphist delete <<<"$result"
            notify-send "$result" -i ~/.config/dunst/icons/status/clip-edit.svg -r 92999 -t 1000 -u normal
            ;;
        11)
            cliphist wipe
            notify-send "Clipbboard History Cleared" -i ~/.config/dunst/icons/status/clip-edit.svg -r 92999 -t 1000 -u normal
            exit
            ;;
    esac
done

