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

#----------#
# Firewall #
#----------#
sudo systemctl enable firewalld.service


#---------#
# Flatpak #
#---------#
sudo flatpak override --filesystem=$HOME/.themes
sudo flatpak override --filesystem=$HOME/.icons

#----------------#
# Create Folders #
#----------------#
mkdir -p ~/.themes ~/.icons ~/Projects ~/Documents ~/Downloads ~/Videos
mkdir -p ~/Pictures/Screenshots
mkdir -p ~/Torrent/{torrents,torrent_files,finished_torrents/{Movie,TV,Music,TT},finished_torrent_files,watched_torrent_files}
sudo mkdir -p /usr/share/themes /usr/share/icons

#---------------------#
# Add User to a Group #
#---------------------#
sudo usermod -aG input $(whoami)   # Adds used user to input group for waybar keyboard-state widget to work
sudo usermod -aG video $(whoami)

#--------------#
# Change Shell #
#--------------#
chsh -s $(which fish)

#----------------------#
# Add Hyprland Plugins #
#----------------------#
hyprpm update
hyprpm add https://github.com/hyprwm/hyprland-plugins
hyprpm enable hyprexpo
