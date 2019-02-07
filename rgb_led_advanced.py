import time
import board
import neopixel
led = neopixel.NeoPixel(board.NEOPIXEL, 10)

led.brightness = 0.3

red = (255, 0, 0)
purple = (255, 0, 255)
off = (0, 0, 0)

while True:
    led[0] = (255, 0, 0)  # You can use numbers or the color names from above
    time.sleep(0.5)
    led[0] = (0, 0, 0)
    led[1] = (red)
    time.sleep(0.5)
    led[1] = (off)
    led[2] = (purple)
    time.sleep(0.5)
    led[2] = (off)
    time.sleep(0.5)