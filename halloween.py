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




color_list = [red, purple, orange, yellow]
def fade_out(color, speed =0.01, ratio = 50):
    #Fades out with a certain color
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
    #Fades in with a certain color
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
        


white = ((255,255,255))
color_list = [purple, orange, yellow]
def sparkle(bg = random.choice(color_list), fg = red, delay = 0.5, spark = 5):
    #Makes individual neopixels to sparkle
    for i in  range(spark):
              won = random.randint(0,29)
              too = random.randint(0,29)
              tree = random.randint(0,29)
              hii = random.randint(0,29)
              who = random.randint(0,29)
              np.fill(bg)
              np[won] = fg
              np[too] = fg
              np[tree] = fg
              np[hii] = fg
              np[who] = fg
              np.show()
              time.sleep(0.3)
             
             
def lightining():
    #Creates a lightning effet by causing it to flicker white
    doo = random.randint(1,50)
    for i in range(doo):
        np.fill(white)
        np.show()
        too = random.randint(1,8)
        doo = doo / 40 
        np.fill(random.choice(color_list))
        np.show()
        time.sleep(doo)        

def fill():
#This fills up the entire strip with a random color
    count = 0
    for i in range(np.n):
        np.fill(black)
    for i in range(i):
        if (i == i-2) % 3 ==0:
            np[i] = (random.choice(color_list))
            np.show()
            time.sleep(0.1)
            count +=1
            
def flame(bg = (yellow), fg = (255,69,0) , delay = 0.1, fire = 4):
    #Creates a flickering effect that resembles flames
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
    rgb = random.choice(color_list)
    fill()
    lightining()
    fade_out(rgb)
    fade_in(rgb)
    sparkle()
    flame()
   
    
