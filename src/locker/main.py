import os
import subprocess
import time

import screenshot
import blur

def read_lock_timeout():
    cfg_path = os.path.expanduser("~/.config/i4/i4timerc")
    try:
        with open(cfg_path, "r") as f:
            value = f.read().strip()
        if value == ".none":
            return None
        return int(value)
    except Exception:
        return 600

lock_timeout = read_lock_timeout()  # seconds
if lock_timeout is None:
    exit()

def get_idle_ms():
    out = subprocess.check_output(["xprintidle"]).decode().strip()
    return int(out)

def get_screen():
    screenshot.main()
    blur.main()

def main():
    while True:
        idle_ms = get_idle_ms()
        if idle_ms >= lock_timeout * 1000:
            get_screen()
            os.system("i3lock -i ./currentscreen.png")
            os.system("rm -f ./currentscreen.png")
            # Prevent immediate re-locking by waiting until user becomes active again
            while get_idle_ms() >= 2000:
                time.sleep(1)
        time.sleep(1)

if __name__ == "__main__":
    main()

