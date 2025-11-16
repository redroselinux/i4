import os
import time

def get_time_till_lock():
    try:
        with open("/home/"+os.getlogin()+"/.config/i4/i4timerc", "r") as f:
            time_till_lock = f.read
        if time_till_lock == ".none":
            exit()
    except Exception:
        time_till_lock = 600
    return time_till_lock

time_till_lock = get_time_till_lock()

def main():
    while True:
        time.sleep(time_till_lock)
        os.system("i3lock -i assets/redrose.png")

if __name__ == "__main__":
    main()
