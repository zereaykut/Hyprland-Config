#!/bin/env bash

status=$(playerctl status 2>/dev/null)

if [ "$status" = "Playing" ]; then
    playerctl metadata --format '{{title}}  󰓇   {{artist}}'
else
    echo ""
fi

