import os

def main():
    path = os.path.abspath("currentscreen.png")
    print("Saving screenshot to:", path)

    os.system("scrot -o "+path)

    if os.path.exists(path):
        print("File exists!")
    else:
        print("File does NOT exist!")
