#ref: https://circuitpython.readthedocs.io/en/4.x/docs/design_guide.html
import digitalio
import board
import time

with digitalio.DigitalInOut(board.D13) as led:
    led.direction = digitalio.Direction.OUTPUT

    for i in range(10):
        led.value = True
        time.sleep(0.5)

        led.value = False
        time.sleep(0.5)
