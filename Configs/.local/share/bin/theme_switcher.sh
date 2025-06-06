#!/bin/env bash

# theme="${'Catppuccin Mocha':-$1}"
theme="${1}"
themeDir="$HOME/.config/hyprdots/themes/$theme/"
# wallSelect="${"$themeDir/Catppuccin Mocha.png":-$2}"
wallSelect="${2}"
configsDir="$HOME/.config/hyprdots/configs/"
cacheDir="$HOME/.cache/hyprdots"

source $themeDir/variables.sh

# environment variables
export HYPRCURSOR_THEME=$CURSOR_THEME
export HYPRCURSOR_SIZE=$CURSOR_SIZE
export XCURSOR_THEME=$CURSOR_THEME
export XCURSOR_SIZE=$CURSOR_SIZE

# gsettings
gsettings set org.gnome.desktop.interface cursor-theme "$CURSOR_THEME"
gsettings set org.gnome.desktop.interface cursor-size $CURSOR_SIZE
gsettings set org.gnome.desktop.interface icon-theme "$ICON_THEME"
gsettings set org.gnome.desktop.interface gtk-theme "$GTK_THEME"
gsettings set org.gnome.desktop.interface color-scheme "$COLOR_SCHEME"

# hyprland
cp -f $themeDir/hypr.theme $HOME/.config/hypr/hyprland/theme.conf
hyprctl setcursor $CURSOR_THEME $CURSOR_SIZE
hyprctl reload 

# hyprlock
cp -f $themeDir/hyprlock.theme $HOME/.config/hypr/hyprlock/theme.conf

# rofi
cp -f $themeDir/rofi.theme $HOME/.config/rofi/theme.rasi

# kitty
cp -f $themeDir/kitty.theme $HOME/.config/kitty/theme.conf

# swww
wall_switcher.sh "$wallSelect"

# gtk 2/3/4
sed "s/{CURSOR_THEME}/$CURSOR_THEME/; s/{ICON_THEME}/$ICON_THEME/; s/{GTK_THEME}/$GTK_THEME/; s/{CURSOR_SIZE}/$CURSOR_SIZE/" $configsDir/gtkrc_2_0.theme > $HOME/.gtkrc-2.0
sed "s/{CURSOR_THEME}/$CURSOR_THEME/" $configsDir/index.theme > $HOME/.icons/default/index.theme
sed "s/{CURSOR_THEME}/$CURSOR_THEME/; s/{ICON_THEME}/$ICON_THEME/; s/{GTK_THEME}/$GTK_THEME/; s/{CURSOR_SIZE}/$CURSOR_SIZE/" $configsDir/gtk_3_settings.theme > $HOME/.config/gtk-3.0/settings.ini
sed "s/{CURSOR_THEME}/$CURSOR_THEME/; s/{ICON_THEME}/$ICON_THEME/; s/{GTK_THEME}/$GTK_THEME/; s/{CURSOR_SIZE}/$CURSOR_SIZE/" $configsDir/gtk_4_settings.theme > $HOME/.config/gtk-4.0/settings.ini

# waybar
cp -f $themeDir/waybar.theme $HOME/.config/waybar/theme.css
killall waybar && waybar &

# kvantum
cp -f $themeDir/kvantum/kvantum.theme $HOME/.config/Kvantum/kv_theme/kv_theme.svg
cp -f $themeDir/kvantum/kvconfig.theme $HOME/.config/Kvantum/kv_theme/kv_theme.kvconfig

# qt
sed "s/{ICON_THEME}/$ICON_THEME/" $configsDir/qt5ct.theme > $HOME/.config/qt5ct/qt5ct.conf
sed "s/{ICON_THEME}/$ICON_THEME/" $configsDir/qt6ct.theme > $HOME/.config/qt6ct/qt6ct.conf

# kde
sed "s/{ICON_THEME}/$ICON_THEME/" $configsDir/kdeglobals.theme > $HOME/.config/kdeglobals

#xsettings
sed "s/{CURSOR_THEME}/$CURSOR_THEME/; s/{ICON_THEME}/$ICON_THEME/; s/{GTK_THEME}/$GTK_THEME/" $configsDir/xsettingsd.theme > $HOME/.config/xsettingsd/xsettingsd.conf

# wlogout
cp -f $themeDir/wlogout.theme $HOME/.config/wlogout/theme.css

# swaync
cp -f $themeDir/swaync.theme $HOME/.config/swaync/theme.css
killall swaync && swaync &

# swayosd
cp -f $themeDir/swayosd.theme $HOME/.config/swayosd/theme.css
killall swayosd-server && swayosd-server &

# hyprlock
# cp -f $wallSelect $HOME/.cache/themes/lock_screen.png
theme_lock_cache.sh "$wallSelect"

# btop
cp -f $themeDir/btop.theme $HOME/.config/btop/themes/btop.theme

# cache variables
mkdir -p $cacheDir

cat << EOF > $cacheDir/theme.sh
#!/bin/env bash
theme="$theme"
EOF

cat << EOF > $cacheDir/wallSelect.sh
#!/bin/env bash
wallSelect="$wallSelect"
EOF