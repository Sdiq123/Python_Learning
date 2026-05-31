
from win10toast import ToastNotifier
import time

toast = ToastNotifier()
REPEAT_INTERVAL = 10      # Repeat frequency in seconds

while True:
    toast.show_toast(
        "Notification",
        "Hey Sadiq Please Keep Drinking water to Stay Hydrated",
        duration = 5,
        icon_path = "icon.ico",
        threaded = True,
    )
    time.sleep(REPEAT_INTERVAL)

# ---> Harry's Code for Mac - OS
# import os
# command = '''osascript -e 'say "Hello World!"'; osascript -e 'display alert "hello world"'''
