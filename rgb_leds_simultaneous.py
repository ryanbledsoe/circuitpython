import board
import neopixel
import time

led = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

led[0] = (10, 0, 0)
led[9] = (0, 10, 0)
led.show()
time.sleep(5)
