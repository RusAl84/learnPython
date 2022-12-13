import os
from datetime import datetime, timedelta, time
import platform


class Config:
    def __init__(self, pair_start=None):
        self.SSH_HOST = "192.168.100.234"
        self.SSH_USER = "rusal"
        self.SSH_PASS = (
            os.environ.get("SIDIB_MON_SHH_PASS") or "SSH pass zadefine odin11!!"
        )
        self.SSH_PATH = "/opt/MIREApython/"

        today = datetime.now()
        if not pair_start:
            self.pair_start = today.replace(hour=12, minute=00)
        else:
            self.pair_start = datetime.combine(
                today.date(), datetime.strptime(pair_start, "%H:%M").time()
            )
        self.pair_end = self.pair_start + timedelta(minutes=90)
        self.env_platform = platform.platform()
        self.env_path = os.path.realpath(os.curdir)

    def print_status_time(self):
        now = datetime.now()
        tdelta = self.pair_end - now
        min_left = f"{tdelta.seconds // 60}:{(tdelta.seconds // 60) % 60}"
        print(
            f"\nLast run at {now.strftime('%X')} \tPair ends at {self.pair_end.strftime('%X')}\tMinutes left: {min_left}"
        )

def print_secret_key():
    print("print_secret_key")
    print(f"Hello, from {__name__}!")