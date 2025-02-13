#!/bin/env bash

# theme="${'Catppuccin Mocha':-$1}"
theme="${1}"
themeDir="$HOME/.config/hyprdots/themes/$theme/"
# wallSelect="${"$themeDir/Catppuccin Mocha.png":-$2}"
wallSelect="${2}"
configsDir="$HOME/.config/hyprdots/configs/"

source $themeDir/variables.sh