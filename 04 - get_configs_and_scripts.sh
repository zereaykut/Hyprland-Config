#!/bin/bash

#----------------#
# Create Folders #
#----------------#
mkdir -p ~/.config
mkdir -p ~/.local/share/{bin,waybar}
mkdir -p ~/.themes ~/.icons ~/Projects ~/Documents ~/Downloads ~/Videos
mkdir -p ~/Pictures/Screenshots
mkdir -p ~/Torrent/{torrents,torrent_files,finished_torrents/{Movie,TV,Music,TT},finished_torrent_files,watched_torrent_files}
sudo mkdir -p /usr/share/themes /usr/share/icons

#------------#
# Get Configs #
#------------#
cp -rf .config/* ~/.config/

#-------------#
# Get Scripts #
#-------------#
cp -rf .local/share/bin/* ~/.local/share/bin/

#--------#
# Pacman #
#--------#
sudo mv move/pacman/pacman.conf /etc/.

#-------#
# Login #
#-------#
sudo mv move/sddm/sddm.conf /etc/.
sudo mkdir /usr/share/sddm/themes/Simple-SDDM
sudo cp -rf move/sddm/Simple-SDDM/* /usr/share/sddm/themes/Simple-SDDM/

#------#
# Grub #
#------#
sudo mv move/grub/grub.conf /etc/default/grub
sudo mv move/grub/grub_background.png /boot/grub/.
sudo grub-mkconfig -o /boot/grub/grub.cfg


