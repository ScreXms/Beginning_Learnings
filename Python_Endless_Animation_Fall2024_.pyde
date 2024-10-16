'''
Victoria Duong
Toolkit-Python.A.Fa.24
Code Assignment #4.a: Create a Endless animation using primitives: circle, square, rectangles, triangles 
2024.10.15
'''

def setup():
    size(1000,1000)
    noStroke()
    frameRate(10)
    
def draw():
    background(0)
    
    shapes = int(random(3))
    size = random(200, 350)
    
# shape coordinates 
    if shapes == 0:
        draw_circle(500, 400, size)
    elif shapes == 1:
        draw_square(500, 700 , size)
    elif shapes == 2:
        draw_triangle(500, 150, size)
            
def draw_circle( x, y, size):
    fill(random_color())
    ellipse(x, y, size, size) 
    
def draw_square(x, y, size):
    fill(random_color())
    rect(x - size/2, y - size/2, size, size)
    
def draw_triangle(x, y, size):
    fill(random_color())
    x1, y1 = x , y - size/2 #top
    x2, y2 = x - size/2, y + size/2 # bottom left
    x3, y3 = x + size/2, y +size/2 # bottom right
    triangle(x1, y1, x2, y2, x3, y3) 
             
    
def random_color():
    return color(random(255), random(255), random(255))
