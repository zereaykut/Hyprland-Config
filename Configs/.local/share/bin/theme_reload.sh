#!/bin/env bash

cacheDir="$HOME/.cache/hyprdots"

source $cacheDir/theme.sh
source $cacheDir/wallSelect.sh

theme_switcher.sh "$theme" "$wallSelect"