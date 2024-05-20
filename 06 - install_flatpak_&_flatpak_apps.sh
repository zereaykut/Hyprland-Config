#!/bin/bash

#-----------------#
# Install Flatpak #
#-----------------#
sudo pacman --needed --noconfirm -S flatpak

#--------#
# Apps   #
#--------#
flatpak install flathub com.valvesoftware.Steam