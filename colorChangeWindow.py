#Andrew Parker
#10/20/17
#colorChangeWindow.py - pops up a window that changes to a random color every time you click it
from ggame import *
from random import randint
randint (0,1)

white = Color(0xFFFFFF,1)
black = Color(0x000000,1)
red = Color(0xFF0000,1) 
yellow = Color(0xFFFF00,1)
orange = Color(0xFFA500,1)
green = Color(0x00FF00,1) 
lightBlue = Color(0x00FFFF,1) 
blue = Color(0x0000FF,1) 
purple = Color(0x7F00FF,1) 
darkPink = Color(0xFF007F,1) 

blackOutline = LineStyle(1,black) #pixels, color
Rectangle = RectangleAsset(970,500,blackOutline,white) #width, height, outline, fill

def mouseClick(event):
    num = randint(1,10)
    if num = 1:
        color = white
    elif num = 2:
        color = black
    elif num = 3:
        color = red
    elif num = 4:
        color = yellow
    elif num = 5:
        color = orange
    elif num = 6:
        color = green
    elif num = 7:
        color = lightBlue
    elif num = 8:
        color = blue
    elif num = 9:
        color = purple
    elif num = 10:
        color = darkPink
        
    rectangle = RectangleAsset(1000,1000,outline,color)

"App().listenMouseEvent('click',mouseClick)"
Sprite(Rectangle,(30,15))
App().run()
