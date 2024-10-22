import board
import time
from neopixel import NeoPixel
import random

np = NeoPixel(board.D2, 30, auto_write = False, brightness=1)



red = ((255,0,0))
blue = ((0,255,0))
green = ((0,0,255))
white = ((255,255,255))
orange = (255,69,0)
yellow = (255,255,10)
def flame(bg = (yellow), fg = (255,69,0) , delay = 0.1, fire = 4):
    for i in  range(fire):
              won = random.randint(0,29)
              too = random.randint(0,29)
              tree = random.randint(0,29)
              forr = random.randint(0,29)
              np.fill(bg)
              np[won] = fg
              np[too] = fg
              np[tree] = fg
              np[forr] = (255,165,0)
              np.show()
              time.sleep(delay)


while True:
    flame()
                         
