#Andrew Parker
#10/20/17
#colorChangeWindow.py - pops up a window that changes to a random color every time you click it
from ggame import *
from random import randint
randint (0,1)

white = Color(0xFFFFFF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels, color
Rectangle = RectangleAsset(970,500,blackOutline,white) #width, height, outline, fill


"App().listenMouseEvent('click',mouseClick)"
Sprite(Rectangle,(30,15))
App().run()



