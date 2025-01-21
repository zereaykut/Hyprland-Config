#!/usr/bin/python
import subprocess as sp


def send_notification(message: str, icon: str, timeout: int = 800, notify_id: int = 92999) -> None:
    sp.run(["notify-send", f'"{message}"', "-i", icon, "-r", str(notify_id), "-t", str(timeout), "-u", "normal"])
