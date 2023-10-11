#!/bin/bash

#---------------#
# Login Manager #
#---------------#
sudo systemctl enable sddm

#-----------#
# Bluetooth #
#-----------#
sudo systemctl enable bluetooth

#-------#
# Audio #
#-------#
systemctl enable --user pipewire-pulse.service

#----------------#
# Create Folders #
#----------------#
mkdir ~/Projects ~/Documents ~/Downloads ~/Videos
mkdir -p ~/Pictures/Screenshots
mkdir -p ~/Torrent/{torrents,torrent_files,finished_torrents,finished_torrent_files,watched_torrent_files}

#--------------#
# Change Shell #
#--------------#
chsh -s $(which zsh)