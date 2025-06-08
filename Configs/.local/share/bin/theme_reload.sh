#!/bin/env bash

cache_path="$HOME/.cache/hyprdots"

source $cache_path/theme.sh
source $cache_path/wall_select.sh

theme_switcher.sh "$theme" "$wall_select"