'''
Victoria Duong
Toolkit-Python.A.Fa24
Code Assignment #5: One Button Game ( Attempt 06)
2024.10.23
''' 

stop_char = True
circleX = 100
circleH = 100
circleLL = 100
circleRL = 200
circleLA = 100
circleRA = 200

circleDirection = 1
circleDirectionH = 1
circleDirectionLL = 1
circleDirectionRL = 1
circleDirectionLA = 1
circleDirectionRA = 1


def setup():
    size(600, 600)
    noStroke()
    frameRate(60)
    
def draw_circle(x, y, size):
    fill(255)
    ellipse(x, y, size, size)

def draw():
    background(30,30,30)
    print(frameCount)
    global circleX, circleDirection, stop_char
    global circleH, circleLL, circleRL, circleLA, circleRA 
    global circleDirectionH, circleDirectionLL, circleDirectionRL, circleDirectionLA, circleDirectionRA

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
 
#TUMMY
    if circleX >= width - 130:
        circleDirection = -3
    elif circleX <= 130:
        circleDirection = 3    
    if stop_char:
        #Draw the Moving Version
     #tummy
        fill(random(255), random(255), random(255))
        ellipse(circleX, 350, 300, 300)
        circleX = circleX + circleDirection   
    else:
        # Draw the Stopped Version
        #tummy
        fill(random(255), random(255), random(255))
        ellipse(circleX, 350, 300, 300)
   
#HEAD    
    if circleH >= width - 75:
        circleDirectionH = -4
    elif circleH <= 75:
        circleDirectionH = 4    
    if stop_char:
        #Draw the Moving Version
     #head
        fill(random(255), random(255), random(255))
        ellipse(circleH, 150, 150, 150)
        circleH = circleH + circleDirectionH   
    else:
        # Draw the Stopped Version
        #head
        fill(random(255), random(255), random(255))
        ellipse(circleH, 150, 150, 150)
        
#LEFT LEG    
    if circleLL >= width - 50:
        circleDirectionLL = -2
    elif circleLL <= 50:
        circleDirectionLL = 2   
    if stop_char:
        #Draw the Moving Version
     #left leg
        fill(random(255), random(255), random(255))
        ellipse(circleLL, 500, 100, 100)
        circleLL = circleLL + circleDirectionLL   
    else:
        # Draw the Stopped Version
        #left leg
        fill(random(255), random(255), random(255))
        ellipse(circleLL, 500, 100, 100)

#RIGHT LEG        
    if circleRL >= width - 50:
        circleDirectionRL = -3
    elif circleRL <= 50:
        circleDirectionRL = 3   
    if stop_char:
        #Draw the Moving Version
     #right leg
        fill(random(255), random(255), random(255))
        ellipse(circleRL, 500, 100, 100)
        circleRL = circleRL + circleDirectionRL   
    else:
        # Draw the Stopped Version
        #right leg
        fill(random(255), random(255), random(255))
        ellipse(circleRL, 500, 100, 100)

#LEFT ARM        
    if circleLA >= width - 35:
        circleDirectionLA = -3
    elif circleLA <= 35:
        circleDirectionLA = 3   
    if stop_char:
        #Draw the Moving Version
     #left arm
        fill(random(255), random(255), random(255))
        ellipse(circleLA, 300, 75, 75)
        circleLA = circleLA + circleDirectionLA   
    else:
        # Draw the Stopped Version
        #left arm
        fill(random(255), random(255), random(255))
        ellipse(circleLA, 300, 75, 75)
        
#RIGHT ARM        
    if circleRA >= width - 35:
        circleDirectionRA = -5
    elif circleRA <= 35:
        circleDirectionRA = 5  
    if stop_char:
        #Draw the Moving Version
     #left arm
        fill(random(255), random(255), random(255))
        ellipse(circleRA, 300, 75, 75)
        circleRA = circleRA + circleDirectionRA   
    else:
        # Draw the Stopped Version
        #left arm
        fill(random(255), random(255), random(255))
        ellipse(circleRA, 300, 75, 75)
        
#EYES
    fill(0)
    ellipse((width/2 - 25), 130, 30, 30) #left eye
    ellipse((width/2 + 25), 130, 30, 30) #right eye
    ellipse((width/2), 180, 40, 10) #mouth
