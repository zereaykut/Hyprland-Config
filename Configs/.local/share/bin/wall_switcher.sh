#!/bin/env bash
cacheDir="$HOME/.cache/hyprdots"
wallSelect="${1}"

swww img "$wallSelect" --transition-type center --transition-fps 60 --transition-duration 3

mkdir -p $cacheDir

cat << EOF > $cacheDir/wallSelect.sh
#!/bin/env bash
wallSelect="$wallSelect"
EOF