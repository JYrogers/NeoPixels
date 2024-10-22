import board
import time
from neopixel import NeoPixel
import random

np = NeoPixel(board.D2, 30, auto_write = False, brightness=3)


red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
orange = (238,96,0)
yellow = (255,255,0)

def flame():
    doo = random.randint(1,50)
    for i in range(doo):
        np.fill(orange)
        np.show()
        too = random.randint(1,8)
        doo = doo / 45
        np.fill(yellow)
        np.show()
        time.sleep(doo)        
while True:
    flame()
