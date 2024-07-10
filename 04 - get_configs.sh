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
sudo mv move/sddm/Ghost.png /usr/share/sddm/themes/sugar-candy/Backgrounds/.
sudo mv move/sddm/theme.conf /usr/share/sddm/themes/sugar-candy/.

#------#
# Grub #
#------#
sudo mv move/grub/grub.conf /etc/default/grub
sudo mv move/grub/grub_background.png /boot/grub/.
sudo grub-mkconfig -o /boot/grub/grub.cfg


