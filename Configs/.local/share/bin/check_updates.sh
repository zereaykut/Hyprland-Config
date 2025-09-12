#!/usr/bin/env bash

# Script to check for updates across pacman, yay, and flatpak, and display the count of updates in Waybar.
# If no updates are available, shows a "Packages are up to date" message.
# Otherwise, displays the number of updates for each package manager (pacman, yay, flatpak) in the tooltip.


pacman_updates=$(checkupdates | wc -l)
yay_updates=$(yay -Qum | wc -l)
flatpak_updates=$(flatpak remote-ls --updates | wc -l)

updates=$(( pacman_updates + yay_updates + flatpak_updates ))

if [ $updates -eq 0 ] ; then
    echo "{\"text\":\"󰮯\", \"tooltip\":\" Packages are up to date\"}"
else
    echo "{\"text\":\"󰮯 $updates\", \"tooltip\":\"󰮯 pacman $pacman_updates\n yay $yay_updates\n flatpak $flatpak_updates \"}"
fi