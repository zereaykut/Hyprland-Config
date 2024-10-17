#!/usr/bin/python
import subprocess as sp


def send_notification(message: str, icon: str, timeout: int = 800) -> None:
    sp.run(
        f"""notify-send "{message}" -i {icon} -r 92999 -t {timeout} -u normal""",
        shell=True,
    )
