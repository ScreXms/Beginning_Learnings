'''
Victoria Duong
Toolkit-Python.A.Fa24
Code Assignment #5: One Button Game ( Attempt 05)
2024.10.23
'''  

stop_char = True
circleX = 100
circleDirection = 1

def setup():
    size(600, 600)
    noStroke()
    frameRate(40)
    
def draw_circle(x, y, size):
    fill(255)
    ellipse(x, y, size, size)

def draw():
    background(30,30,30)
    print(frameCount)
    global circleX, circleDirection, stop_char

    if keyPressed and key == ' ':
        stop_char = False
    else:
        stop_char = True
        
    fill(255)
    draw_circle(width/2, 350, 300) #tummy
    draw_circle(width/2, 150, 150) #head
    draw_circle((width/2 - 75), 500, 100) #left leg
    draw_circle((width/2 + 75), 500, 100) #right leg
    draw_circle((width/2 - 120), 300, 75) #left arm
    draw_circle((width/2 + 120), 300, 75) #right arm
 
    if circleX >= width - 130:
        circleDirection = -1
    elif circleX <= 130:
        circleDirection = 1

    
    if stop_char:
        #Draw the Moving Version
     #tummy
        fill(random(255), random(255), random(255))
        ellipse(circleX, 350, 300, 300)
        circleX = circleX + circleDirection    
        
    # #head
        fill(random(255), random(255), random(255))
        ellipse(circleX, 150, 150, 150)
        circleX = circleX + circleDirection
    
    # #left leg
        fill(random(255), random(255), random(255))
        ellipse(circleX - 75, 500, 100, 100)
        circleX = circleX + circleDirection
    
    # #right leg
        fill(random(255), random(255), random(255))
        ellipse(circleX + 75, 500, 100, 100)
        circleX = circleX + circleDirection
    
    # #left arm
        fill(random(255), random(255), random(255))
        ellipse(circleX - 120, 300, 75, 75)
        circleX = circleX + circleDirection
    
    # #right arm
        fill(random(255), random(255), random(255))
        ellipse(circleX + 120, 300, 75, 75)
        circleX = circleX + circleDirection
                                      
    else:
        # Draw the Stopped Version
        #tummy
        fill(random(255), random(255), random(255))
        ellipse(circleX, 350, 300, 300)
        # #head
        fill(random(255), random(255), random(255))
        ellipse(circleX, 150, 150, 150)
        # #left leg
        fill(random(255), random(255), random(255))
        ellipse(circleX - 75, 500, 100, 100)
        # #left leg
        fill(random(255), random(255), random(255))
        ellipse(circleX - 75, 500, 100, 100)
        # #right leg
        fill(random(255), random(255), random(255))
        ellipse(circleX + 75, 500, 100, 100)
        # #left arm
        fill(random(255), random(255), random(255))
        ellipse(circleX - 120, 300, 75, 75)
        # #right arm
        fill(random(255), random(255), random(255))
        ellipse(circleX + 120, 300, 75, 75)
        
    
    fill(0)
    ellipse((width/2 - 25), 130, 30, 30) #left eye
    ellipse((width/2 + 25), 130, 30, 30) #right eye
    ellipse((width/2), 180, 40, 10) #mouth
