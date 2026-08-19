import time
from plyer import notification

while True:
    print("Drink Some Water")
    notification.notify("Plz drink water", message="It's Time for you to drink Water")
    time.sleep(60*60)   