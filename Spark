import board
import time
from neopixel import NeoPixel
import random

np = NeoPixel(board.D2, 30, auto_write = False, brightness=1)



red = ((255,0,0))
blue = ((0,255,0))
green = ((0,0,255))
white = ((255,255,255))
color_list = [red,blue,green]
def sparkle(bg = (30,0,0), fg = white, delay = 0.5, spark = 3):
    for i in  range(spark):
              won = random.randint(0,29)
              too = random.randint(0,29)
              tree = random.randint(0,29)
              np.fill(bg)
              np[won] = fg
              np[too] = fg
              np[tree] = fg
              np.show()
              time.sleep(delay)


while True:
    sparkle()
                         
