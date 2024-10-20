#!/usr/bin/python

import subprocess as sp
import time

import psutil

BATTERY_CRITICAL = 20
BATTERY_URGENT = 30


def secs2hours(secs: int) -> str:
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)


def get_battery_info() -> dict:
    battery_info = psutil.sensors_battery()
    return {
        "percent": round(battery_info.percent, 2),
        "secsleft": secs2hours(battery_info.secsleft),
        "power_plugged": battery_info.power_plugged,
    }


def send_notification(message: str, icon: str, timeout: int = 800, urgency:str = "normal") -> None:
    sp.run(
        f"""dunstify "{message}" -i {icon} -r 92999 -t {timeout} -u {urgency}""",
        shell=True,
    )


if __name__ == "__main__":
    user = sp.run("whoami", shell=True, capture_output=True, text=True).stdout.strip()
    while True:
        battery_info = get_battery_info()
        plugged = battery_info["power_plugged"]
        if (battery_info["percent"] <= BATTERY_URGENT) & (not plugged):
            send_notification(
                f"""Percentage: {battery_info["percent"]}%\nPlugged:{battery_info["power_plugged"]}""",
                f"/home/{user}/.config/dunst/icons/status/battery-status.png",
                10000,
                "normal"
            )
            time.sleep(10)
        elif (battery_info["percent"] <= BATTERY_CRITICAL) & (not plugged):
            send_notification(
                f"""Percentage: {battery_info["percent"]}%\nPlugged:{battery_info["power_plugged"]}""",
                f"/home/{user}/.config/dunst/icons/status/battery-status.png",
                10000,
                "critical"
            )
            time.sleep(10)
        else:
            time.sleep(60)
