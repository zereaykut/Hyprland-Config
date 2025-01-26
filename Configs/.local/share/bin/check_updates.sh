#!/usr/bin/env bash

pacUpds=$(checkupdates | wc -l)
yayUpds=$(yay -Qum | wc -l)
flatUpds=$(flatpak remote-ls --updates | wc -l)

upds=$(( pacUpds + yayUpds + flatUpds ))

if [ $upds -eq 0 ] ; then
    echo "{\"text\":\"󰮯\", \"tooltip\":\" Packages are up to date\"}"
else
    echo "{\"text\":\"󰮯 $upds\", \"tooltip\":\"󰮯 pacman $pacUpds\n yay $yayUpds\n flatpak $flatUpds \"}"
fi