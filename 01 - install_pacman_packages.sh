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
sudo pacman --needed --noconfirm -S python-pyquery
sudo pacman --needed --noconfirm -S pyenv

#----------#
# Hyprland #
#----------#
sudo pacman --needed --noconfirm -S hyprland
sudo pacman --needed --noconfirm -S xdg-desktop-portal-hyprland
sudo pacman --needed --noconfirm -S xdg-desktop-portal-gtk
sudo pacman --needed --noconfirm -S qt5-wayland
sudo pacman --needed --noconfirm -S qt6-wayland

#------------#
# Screenlock #
#------------#
sudo pacman --needed --noconfirm -S hyprlock

#----------------------#
# Authentication Agent #
#----------------------#
sudo pacman --needed --noconfirm -S polkit-gnome

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

#------------------------#
# Filesystem / Partition #
#------------------------#
sudo pacman --needed --noconfirm -S exfatprogs
sudo pacman --needed --noconfirm -S partitionmanager

#-----------#
# Top Panel #
#-----------#
sudo pacman --needed --noconfirm -S waybar

#----------#
# Terminal #
#----------#
sudo pacman --needed --noconfirm -S kitty
sudo pacman --needed --noconfirm -S btop      # Resource monitor that shows usage and stats for processor, memory, disks, network and processes.
sudo pacman --needed --noconfirm -S eza       # A modern, maintained replacement for ls.
sudo pacman --needed --noconfirm -S fastfetch # System info
sudo pacman --needed --noconfirm -S lazygit   # Cli git ui
sudo pacman --needed --noconfirm -S dust      # du + rust = dust. Like du but more intuitive.
sudo pacman --needed --noconfirm -S atuin     # Search shell history better
sudo pacman --needed --noconfirm -S fd        # Faster, colorized alternative to find
sudo pacman --needed --noconfirm -S bat       # Smarter cat with syntax highlighting
sudo pacman --needed --noconfirm -S zoxide    # zoxide is a smarter cd command, inspired by z and autojump.
sudo pacman --needed --noconfirm -S fzf       # Fuzzy finder

#-------------#
# Text Editor #
# ------------#
sudo pacman --needed --noconfirm -S neovim
sudo pacman --needed --noconfirm -S npm
sudo pacman --needed --noconfirm -S unzip

#-----------------#
# Hyprland Plugin #
#-----------------#
sudo pacman --needed --noconfirm -S meson
sudo pacman --needed --noconfirm -S cmake
sudo pacman --needed --noconfirm -S cpio
sudo pacman --needed --noconfirm -S hyprwayland-scanner

#------#
# Apps #
#------#
sudo pacman --needed --noconfirm -S vlc
sudo pacman --needed --noconfirm -S bitwarden
sudo pacman --needed --noconfirm -S gimp
sudo pacman --needed --noconfirm -S gwenview
sudo pacman --needed --noconfirm -S qbittorrent
sudo pacman --needed --noconfirm -S thunderbird
sudo pacman --needed --noconfirm -S notepadqq
# sudo pacman --needed --noconfirm -S obs-studio
sudo pacman --needed --noconfirm -S okular
sudo pacman --needed --noconfirm -S ark
# sudo pacman --needed --noconfirm -S discord
sudo pacman --needed --noconfirm -S obsidian
sudo pacman --needed --noconfirm -S libreoffice-fresh
sudo pacman --needed --noconfirm -S kdeconnect
sudo pacman --needed --noconfirm -S solaar
sudo pacman --needed --noconfirm -S qalculate-gtk
sudo pacman --needed --noconfirm -S kwalletmanager
sudo pacman --needed --noconfirm -S timeshift

#----------#
# QT / KDE #
#----------#
sudo pacman --needed --noconfirm -S qt5ct
sudo pacman --needed --noconfirm -S qt6ct
sudo pacman --needed --noconfirm -S kvantum
sudo pacman --needed --noconfirm -S kvantum-qt5

sudo pacman --needed --noconfirm -S dolphin
sudo pacman --needed --noconfirm -S kservice5
sudo pacman --needed --noconfirm -S kde-cli-tools
sudo pacman --needed --noconfirm -S kdegraphics-thumbnailers
sudo pacman --needed --noconfirm -S ffmpegthumbs
sudo pacman --needed --noconfirm -S archlinux-xdg-menu           # for mimeapps.list to show on dolphin

#----------#
# Clipoard #
#----------#
sudo pacman --needed --noconfirm -S wl-clipboard
sudo pacman --needed --noconfirm -S cliphist

#--------------#
# Checkupdates #
#--------------#
sudo pacman --needed --noconfirm -S pacman-contrib

#-------#
# Power #
#-------#
sudo pacman --needed --noconfirm -S upower

#-----#
# VPN #
#-----#
sudo pacman --needed --noconfirm -S openvpn

#----------#
# Firewall #
#----------#
sudo pacman --needed --noconfirm -S firewalld

#--------------#
# Notification #
#--------------#
sudo pacman --needed --noconfirm -S dunst

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
sudo pacman --needed --noconfirm -S fish
sudo pacman --needed --noconfirm -S starship
sudo pacman --needed --noconfirm -S fisher

#------------------#
# Containerization #
#------------------#
sudo pacman --needed --noconfirm -S docker

#-----------------#
# Install Flatpak #
#-----------------#
sudo pacman --needed --noconfirm -S flatpak

#--------#
# Gaming #
#--------#
sudo pacman --needed --noconfirm -S gamescope
sudo pacman -S steam
