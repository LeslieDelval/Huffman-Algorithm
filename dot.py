from bluedot import BlueDot
from signal import pause
import time

def unlock():
    print("Unlocking")
    time.sleep(3)
    print("Locking")

bd = BlueDot()
bd.when_pressed = unlock

pause()
