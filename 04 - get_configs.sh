#!/bin/bash

#------------#
# Get .config #
#------------#
cp -rf .config/* $HOME/.config/

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


