#!/bin/env bash

# Read battery status and level
status=$(cat /sys/class/power_supply/BAT1/status)
level=$(cat /sys/class/power_supply/BAT1/capacity)

# Define icons for different battery levels (0-9)
icons=(
    "󰛞 󱢠 󱢠 󱢠 󱢠 "
    "󰣐 󱢠 󱢠 󱢠 󱢠 "
    "󰣐 󰛞 󱢠 󱢠 󱢠 "
    "󰣐 󰣐 󱢠 󱢠 󱢠 "
    "󰣐 󰣐 󰛞 󱢠 󱢠 "
    "󰣐 󰣐 󰣐 󱢠 󱢠 "
    "󰣐 󰣐 󰣐 󰛞 󱢠 "
    "󰣐 󰣐 󰣐 󰣐 󱢠 "
    "󰣐 󰣐 󰣐 󰣐 󰛞 "
    "󰣐 󰣐 󰣐 󰣐 󰣐 "
)

# Determine the appropriate icon index
i=$((level / 10))
[[ "$i" -gt 9 ]] && i=9

# Output charging symbol if charging
[[ "$status" == "Charging" ]] && printf " "

# Output the battery icon
printf "%s\n" "${icons[$i]}"

