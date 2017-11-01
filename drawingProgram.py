#Andrew Parker
#11/1/17
#drawingProgram - draws stuff

from ggame import *

#constants 
ROWS = 24
COLS = 50
CELL_SIZE = 20


black = Color(0x000000,1)
blackOutline = LineStyle(1,black)
startBox = RectangleAsset(CELL_SIZE, CELL_SIZE,LineStyle(1,black),black)



rectangle = RectangleAsset(970,500,blackOutline,black)
Sprite(rectangle,(25,15))


"""
if __name__ == '__main__':"""


    


