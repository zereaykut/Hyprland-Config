#!/usr/bin/env bash

pacman_updates=$(checkupdates | wc -l)
yay_updates=$(yay -Qum | wc -l)
flatpak_updates=$(flatpak remote-ls --updates | wc -l)

updates=$(( pacman_updates + yay_updates + flatpak_updates ))

if [ $updates -eq 0 ] ; then
    echo "{\"text\":\"󰮯\", \"tooltip\":\" Packages are up to date\"}"
else
    echo "{\"text\":\"󰮯 $updates\", \"tooltip\":\"󰮯 pacman $pacman_updates\n yay $yay_updates\n flatpak $flatpak_updates \"}"
fi