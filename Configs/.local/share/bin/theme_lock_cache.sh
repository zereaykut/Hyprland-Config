#!/bin/env bash

# Input file (could be any image file path)
wallDir="$1"
cacheDir="$HOME/.cache/themes"

mkdir -p $cacheDir

# Check if the input file exists
if [ ! -f "$wallDir" ]; then
    echo "File does not exist!"
    exit 1
fi

# Get the file extension
fileExtension="${wallDir##*.}"

# Check if ImageMagick is installed with 'convert' or 'magick'
if command -v convert &> /dev/null; then
    command="convert"
elif command -v magick &> /dev/null; then
    command="magick"
else
    echo "Neither 'convert' nor 'magick' command found. Please install ImageMagick."
    exit 1
fi

# Check if the file is already a PNG
if [ "${fileExtension,,}" == "png" ]; then
    # If it's a PNG, just copy it to the .cache/themes folder
    cp "$wallDir" "$cacheDir/lock_screen.png"
    echo "PNG image copied to $cacheDir/lock_screen.png"
else
    # Otherwise, convert the image to PNG using ImageMagick and copy it to the folder
    $command "$wallDir[0]" "$cacheDir/lock_screen.png"
    echo "Image converted to PNG and copied to $cacheDir"
fi
