import os
import subprocess
import time

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

lock_timeout = read_lock_timeout()
if lock_timeout is None:
    exit()

def get_idle_ms():
    out = subprocess.check_output(["xprintidle"]).decode().strip()
    return int(out)

def main():
    while True:
        idle_ms = get_idle_ms()
        if idle_ms >= lock_timeout * 1000:
            os.system("i3lock -i assets/redrose.png")
            while get_idle_ms() >= 2000:
                time.sleep(1)
        time.sleep(1)

if __name__ == "__main__":
    main()
