

car_x = 0
car_y = 0

def drawLandscape():
    fill(100, 255, 100)
    #x1, y1, x2, y2, x3, y3
    triangle(200, 350, 0, 600, 350, 600)
    triangle(450, 300, 250, 600, 600, 600 )
    
    fill("#DCFA00")
    ellipse(500, 100, 150, 150)
    pass
    
def drawCar():
    fill("#AB13CE")
    rect(car_x, car_y, 100, 50)
    fill(0)
    ellipse(car_x, car_y + 58, 50, 50)
    fill(0)
    ellipse(car_x + 100, car_y + 58, 50, 50)
    
def moveCar(dir_x, dir_y, speed):
    global car_x, car_y
    car_x += dir_x * speed
    car_y += dir_y * speed
