#!/usr/bin/bash
python -m venv ~/.config/theme-manager/venv
source ~/.config/theme-manager/venv/bin/activate
pip install -r ~/.config/theme-manager/requirements.txt
deactivate