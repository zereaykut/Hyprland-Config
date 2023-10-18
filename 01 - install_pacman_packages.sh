#!/bin/bash

#---------------#
# Base Packages #
#---------------#
sudo pacman --needed --noconfirm -S git
sudo pacman --needed --noconfirm -S base-devel

#--------#
# Python #
#--------#
sudo pacman --needed --noconfirm -S python
sudo pacman --needed --noconfirm -S python-pip
sudo pacman --needed --noconfirm -S python-psutil
sudo pacman --needed --noconfirm -S python-rich
sudo pacman --needed --noconfirm -S python-click

#----------#
# Hyprland #
#----------#
sudo pacman --needed --noconfirm -S hyprland
sudo pacman --needed --noconfirm -S xdg-desktop-portal-hyprland
sudo pacman --needed --noconfirm -S xdg-desktop-portal-gtk
sudo pacman --needed --noconfirm -S qt5-wayland
sudo pacman --needed --noconfirm -S qt6-wayland

#----------------------#
# Authentication Agent #
#----------------------#
sudo pacman --needed --noconfirm -S polkit-kde-agent

#-------#
# Login #
#-------#
sudo pacman --needed --noconfirm -S sddm

#-------------------#
# Screen Brightness #
#-------------------#
sudo pacman --needed --noconfirm -S brightnessctl

#-----------#
# Bluetooth #
#-----------#
sudo pacman --needed --noconfirm -S bluez
sudo pacman --needed --noconfirm -S bluez-utils
sudo pacman --needed --noconfirm -S blueman

#-------#
# Audio #
#-------#
sudo pacman --needed --noconfirm -S pipewire
sudo pacman --needed --noconfirm -S pipewire-alsa
sudo pacman --needed --noconfirm -S pipewire-jack
sudo pacman --needed --noconfirm -S pipewire-pulse
sudo pacman --needed --noconfirm -S gst-plugin-pipewire
sudo pacman --needed --noconfirm -S libpulse
sudo pacman --needed --noconfirm -S sof-firmware
sudo pacman --needed --noconfirm -S alsa-firmware
sudo pacman --needed --noconfirm -S pavucontrol
sudo pacman --needed --noconfirm -S pamixer
sudo pacman --needed --noconfirm -S wireplumber

#-----------#
# Top Panel #
#-----------#
sudo pacman --needed --noconfirm -S waybar

#-----------#
# Wallpaper #
#-----------#
sudo pacman --needed --noconfirm -S hyprpaper

#----------#
# Terminal #
#----------#
sudo pacman --needed --noconfirm -S kitty
sudo pacman --needed --noconfirm -S alacritty
sudo pacman --needed --noconfirm -S htop
sudo pacman --needed --noconfirm -S exa
sudo pacman --needed --noconfirm -S neofetch

#------#
# Apps #
#------#
sudo pacman --needed --noconfirm -S neovim
sudo pacman --needed --noconfirm -S vlc
sudo pacman --needed --noconfirm -S librewolf
sudo pacman --needed --noconfirm -S bitwarden
sudo pacman --needed --noconfirm -S gimp
sudo pacman --needed --noconfirm -S gwenview
sudo pacman --needed --noconfirm -S qbittorrent
sudo pacman --needed --noconfirm -S thunderbird
sudo pacman --needed --noconfirm -S notepadqq
sudo pacman --needed --noconfirm -S obs-studio
sudo pacman --needed --noconfirm -S okular
sudo pacman --needed --noconfirm -S ark
sudo pacman --needed --noconfirm -S discord
sudo pacman --needed --noconfirm -S obsidian
sudo pacman --needed --noconfirm -S libreoffice-fresh

#--------------#
# File Manager #
#--------------#
sudo pacman --needed --noconfirm -S dolphin
sudo pacman --needed --noconfirm -S kdegraphics-thumbnailers
sudo pacman --needed --noconfirm -S ffmpegthumbs

#------#
# Rofi #
#------#
sudo pacman --needed --noconfirm -S rofi
sudo pacman --needed --noconfirm -S rofi-calc
sudo pacman --needed --noconfirm -S rofi-emoji

#------------#
# ScreenShot #
#------------#
sudo pacman --needed --noconfirm -S grim
sudo pacman --needed --noconfirm -S slurp
sudo pacman --needed --noconfirm -S swappy

#----------#
# Clipoard #
#----------#
sudo pacman --needed --noconfirm -S wl-clipboard
sudo pacman --needed --noconfirm -S cliphist
sudo pacman --needed --noconfirm -S hyprland

#-------#
# Power #
#-------#

#----------#
# Firewall #
#----------#
#sudo pacman --needed --noconfirm -S ufw

#--------------#
# Notification #
#--------------#
sudo pacman --needed --noconfirm -S dunst

#---------------#
# Theme / Icons #
#---------------#
sudo pacman --needed --noconfirm -S qt5ct

#-------#
# Fonts #
#-------#
sudo pacman --needed --noconfirm -S ttf-font-awesome
sudo pacman --needed --noconfirm -S ttf-fira-sans
sudo pacman --needed --noconfirm -S ttf-fira-code
sudo pacman --needed --noconfirm -S ttf-firacode-nerd
sudo pacman --needed --noconfirm -S ttf-jetbrains-mono-nerd
sudo pacman --needed --noconfirm -S ttf-jetbrains-mono

#-------#
# Shell #
#-------#
sudo pacman --needed --noconfirm -S zsh

#--------#
# Gaming #
#--------#
sudo pacman --needed --noconfirm -S gamescope
sudo pacman --needed --noconfirm -S lutris
sudo pacman -S steam
