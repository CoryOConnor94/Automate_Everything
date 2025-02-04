from mss import mss
from datetime import datetime
import time

interval = 10

while True:
    with mss() as screen:
        filepath = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        screen.shot(output=filepath)
    print(filepath)
    time.sleep(interval)