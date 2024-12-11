'''
Victoria Duong
Code-Toolkit-Python.A.Fa24
Code Assignment #2: Generative Pattern
2024.10.01
'''

# Circles
loop_frame = 2000

def setup():
    size(600,600)
    background(30,30,30)
    rectMode(CENTER)

def draw():
    background(30,30,30)
    pushMatrix()
    translate(width/2, height/2) # centers rect
    angle = map(frameCount%loop_frame, 0, loop_frame, 0, TWO_PI)
    rotate(angle)
    pushMatrix()
    scale_y = scale_x = map(frameCount%loop_frame, 0, loop_frame, 0.1, 2)
    scale(scale_x, scale_y)
    pushMatrix()
    fill("#FC1414") # red
    stroke(0, 0, 0)
    ellipse(0, 0, 400, 400)
    popMatrix()
    fill("#20E5F5") # blue
    stroke(0, 0, 0)
    ellipse(0, 0, 300, 300)
    popMatrix()
    fill("#9826E0") # purple
    stroke(0, 0, 0)
    ellipse(0, 0, 200, 200)   
    popMatrix()

# Squares
loop_frame = 2000

def setup():
    size(600,600)
    background(30,30,30)
    rectMode(CENTER)

def draw():
    background(30,30,30)
    pushMatrix()
    translate(width/2, height/2) # centers rect
    angle = map(frameCount%loop_frame, 0, loop_frame, 0, TWO_PI)
    rotate(angle)

    pushMatrix()
    scale_y = scale_x = map(frameCount%loop_frame, 0, loop_frame, 0.1, 2)
    scale(scale_x, scale_y)
    
    pushMatrix()
    fill("#FC1414") # red
    stroke(0, 0, 0)
    rect(0, 0, 400, 400)
    # ellipse(0, 0, 400, 400)
    
    popMatrix()
    fill("#20E5F5") # blue
    stroke(0, 0, 0)
    rect(0, 0, 300, 300)
    # ellipse(0, 0, 300, 300)
    
    popMatrix()
    fill("#9826E0") # purple
    stroke(0, 0, 0)
    rect(0, 0, 200, 200)
    # ellipse(0, 0, 200, 200)   
    
    popMatrix()
