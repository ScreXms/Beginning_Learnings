

from background import *

def setup():
    size(600,600)
    background("#66C1EA")

def draw():
    # Pretend that in here
    # I have many many commands
    # to draw a landscape.
    background("#66C1EA")
    drawLandscape()
    drawCar()
    
    
    
def keyPressed():
    if key == 'a':
        moveCar(-1, 0, 5)
    if key == 'd':
        moveCar(1, 0, 5)
    if key == 'w':
        moveCar(0, -1, 5)
    if key == 's':
        moveCar(0, 1, 5)
    
