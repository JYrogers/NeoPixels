import board
import time
from neopixel import NeoPixel
import random

np = NeoPixel(board.D2, 30, auto_write = False, brightness=1)



red = ((255,0,0))
blue = ((0,255,0))
green = ((0,0,255))

color_list = [red,blue,green]
def fade_out(color, speed =0.01, ratio = 50):
    red_ratio = color[0] / ratio
    red_orig = color[0]
    blue_ratio = color[1] / ratio
    blue_orig = color[1]
    green_ratio = color[2] / ratio
    green_orig = color[2]
    for i in range(1,51):
        rd = red_orig - i * red_ratio
        blu = blue_orig - i*blue_ratio
        gren = green_orig - i*green_ratio
        np.fill((rd,blu,gren))
        np.show()
        time.sleep(speed)
       
       
def fade_in(colors, speed = 0.01, ratio = 50):
    red_ratio = colors[0] / ratio
    red_orig = colors[0]
    blue_ratio = colors[1] / ratio
    blue_orig = colors[1]
    green_ratio = colors[2] / ratio
    green_orig = colors[2]    
    for i in range(1,51):
        re = red_orig + i * red_ratio
        ble = blue_orig + i * blue_ratio
        grn = green_orig + i * green_ratio
        np.fill((re,ble,grn))
        np.show()
        time.sleep(speed)
    
    
while True:
          rgb = random.choice(color_list)
          fade_in(rgb)
          fade_out(rgb)
