#!/usr/bin/env bash

# Update system as follows with pacman, yay, and flatpak

sudo pacman -Syu
yay -Syu
flatpak update

# refreshes the module so after you update it will reset to zero
trap 'pkill -RTMIN+20 waybar' EXIT