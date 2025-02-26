#!/usr/bin/env bash

# ========================================================== >> Create Folders
mkdir -p ~/.config
mkdir -p ~/.local/share/{bin,waybar,themes}
mkdir -p ~/Projects ~/Documents ~/Downloads ~/Videos
mkdir -p ~/Pictures/Screenshots
mkdir -p ~/Torrent/{torrents,torrent_files,finished_torrents/{Movie,TV,Music,Comic,Animation,Other},finished_torrent_files,watched_torrent_files}

# ========================================================== >> Configs
cp -rf .config/* ~/.config/

# ========================================================== >> Scripts
cp -rf .local/share/bin/* ~/.local/share/bin/

# ========================================================== >> SDDM
sudo mv ../move/sddm/sddm.conf /etc/.
sudo mkdir /usr/share/sddm/themes/SDDM-hyprdots
sudo cp -rf ../move/sddm/SDDM-hyprdots/* /usr/share/sddm/themes/SDDM-hyprdots/

# ========================================================== >> Cursor
sudo mv ../move/icons_default/index.theme /usr//share/icons/default/index.theme

# ========================================================== >> Grub
sudo mv ../move/grub/grub.conf /etc/default/grub
sudo mv ../move/grub/grub_background.png /boot/grub/.
sudo grub-mkconfig -o /boot/grub/grub.cfg


