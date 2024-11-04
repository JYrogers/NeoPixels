import board
import time
from neopixel import NeoPixel
import random

np = NeoPixel(board.D2, 30, auto_write = False, brightness=1)


i = 29
b = 0

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
orange = (238,96,0)
yellow = (255,255,0)
white = ((255,255,255))
black = ((0,0,0))
purple = ((75,0,150))




color_list = [white, purple, green, blue]
def wipe():
#This fills up the entire strip with a random color
    for i in range(np.n):
        if (i == i-2) % 3 ==0:
            np[i] = (orange)
            np.show()
            time.sleep(0.01)
            
def pattern():
    for i in range(np.n - 1,-1,-1):
        if (i == i-2) % 3 ==0:
            np[i] = color_list[i%len(color_list)]
            np.show()
            time.sleep(0.01)
    
def reversewipe():
    for i in range(np.n - 1 , -1 , -1):
        if (i == i-2) % 3 ==0:
            np[i] = (red)
            np.show()
            time.sleep(0.01)
            
            
def patternback():
    for i in range(np.n):
        if (i == i-2) % 3 ==0:
            np[i] = (random.choice(color_list))
            np.show()
            time.sleep(0.01)
    
    
            


        
            
    
    
            





           
             
             


    
    
while True:
    wipe()
    pattern()
    reversewipe()
    patternback()
   
    
