#!/bin/bash

#------------#
# GTK Themes #
#------------#
tar -xzvf .themes/GTK_themes.tar.gz -C ~/.themes

sudo tar -xzvf .themes/GTK_themes.tar.gz -C /usr/share/themes

#----------------------#
# Icon & Cursor Themes #
#----------------------#
tar -xzvf .themes/Icon_Cursor_themes.tar.gz -C ~/.icons

sudo tar -xzvf .icons/Icon_Cursor_themes.tar.gz -C /usr/share/icons
