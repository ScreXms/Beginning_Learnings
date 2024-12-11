# '''
# Victoria Duong
# Toolkit-Python.A.Fa24
# Code Assignment #5: One Button Game ( Attempt 04)
# 2024.10.23
# '''  

# stop_char = True

# circleDirectionX = 1
# circleDirectionH = 1
# circleDirectionLL = 1
# circleDirectionRL = 1
# circleDirectionLA = 1
# circleDirectionRA = 1

# circleX = 100
# circleH = 150 
# circleLL = 50
# circleRL = 100
# circleLA = 35
# circleRA = 70

# # colorX = (random(255), random(255), random(255))
# # colorH = (random(255), random(255), random(255))
# # colorLL = (random(255), random(255), random(255))
# # colorRL = (random(255), random(255), random(255))
# # colorLA = (random(255), random(255), random(255))
# # colorRA = (random(255), random(255), random(255))

# def setup():
#     size(600, 600)
#     noStroke()
#     frameRate(20)
    
# def draw_circle(x, y, size):
#     fill(255)
#     ellipse(x, y, size, size)

# def draw():
#     background(30,30,30)
#     print(frameCount)
#     global stop_char, circleDirectionX
#     # global circleDirectionX, circleDirectionH, circleDirectionLL, circleDirectionRL, circleDirectionLA, circleDirectionRA
#     # global circleX, circleH, circleLL, circleRL, circleLA, circleRA
#     # global colorX, colorH, colorLL, colorRL, colorLA, colorRA

#     if keyPressed and key == ' ':
#         stop_char = False
#     else:
#         stop_char = True
        
#     fill(255)
#     draw_circle(width/2, 350, 300) #tummy
#     draw_circle(width/2, 150, 150) #head
#     draw_circle((width/2 - 75), 500, 100) #left leg
#     draw_circle((width/2 + 75), 500, 100) #right leg
#     draw_circle((width/2 - 120), 300, 75) #left arm
#     draw_circle((width/2 + 120), 300, 75) #right arm
    
#     if circleX >= width - 130:
#         circleDirectionX = -1
#     elif circleX <= 130:
#         circleDirectionX = 1
        
#     # if circleH >= width - 150:
#     #     circleDirection = -1
#     # elif circleH <= 150:
#     #     circleDirection = 1
        
#     # if circleLL >= width - 50:
#     #     circleDirection = -1
#     # elif circleLL <= 50:
#     #     circleDirection = 1
        
#     # if circleRL >= width - 100:
#     #     circleDirection = -1
#     # elif circleRL <= 100:
#     #     circleDirection = 1
        
#     # if circleLA >= width - 35:
#     #     circleDirection = -1
#     # elif circleLA <= 35:
#     #     circleDirection = 1
        
#     # if circleRA >= width - 70:
#     #     circleDirection = -1
#     # elif circleRA <= 70:
#     #     circleDirection = 1
        
#     if stop_char:
#         #Draw the Moving Version
#     # #tummy
#         ellipse(x, y, size, size)    
#         fill(random(255), random(255), random(255))
#         ellipse(circleX, 350, 300, 300)
#         circleX = circleX + circleDirectionX 

#     # #head
#         fill(random(255), random(255), random(255))
#         ellipse(circleX, 150, 150, 150)
#         circleH = circleX + circleDirectionx
    
#     # #left leg
#         fill(random(255), random(255), random(255))
#         ellipse(circleX - 75, 500, 100, 100)
#         circleLL = circleX + circleDirectionX
    
#     # #right leg
#         fill(random(255), random(255), random(255))
#         ellipse(circleX + 75, 500, 100, 100)
#         circleX = circleX + circleDirectionX
    
#     # #left arm
#         fill(random(255), random(255), random(255))
#         ellipse(circleX - 120, 300, 75, 75)
#         circleX = circleX + circleDirectionX
    
#     # #right arm
#         fill(random(255), random(255), random(255))
#         ellipse(circleX + 120, 300, 75, 75)
#         circleX = circleX + circleDirectionX
        
#     # # #tummy
#     #     ellipse(x, y, size, size)    
#     #     fill(random(255), random(255), random(255))
#     #     ellipse(circleX, 350, 300, 300)
#     #     circleX = circleX + circleDirection 

#     # # #head
#     #     fill(random(255), random(255), random(255))
#     #     ellipse(circleH, 150, 150, 150)
#     #     circleH = circleH + circleDirection
    
#     # # #left leg
#     #     fill(random(255), random(255), random(255))
#     #     ellipse(circleLL - 75, 500, 100, 100)
#     #     circleLL = circleLL + circleDirection
    
#     # # #right leg
#     #     fill(random(255), random(255), random(255))
#     #     ellipse(circleRA + 75, 500, 100, 100)
#     #     circleX = circleX + circleDirection
    
#     # # #left arm
#     #     fill(random(255), random(255), random(255))
#     #     ellipse(circleLA - 120, 300, 75, 75)
#     #     circleX = circleX + circleDirection
    
#     # # #right arm
#     #     fill(random(255), random(255), random(255))
#     #     ellipse(circleRA + 120, 300, 75, 75)
#     #     circleX = circleX + circleDirection
                                      
#     else:
#         # Draw the Stopped Version
#         # ellipse(x, y, size, size) # freezes not only color but motion as well
#         #tummy
#         # fill(r   andom(255), random(255), random(255))
#         ellipse(circleX, 350, 300, 300)
        
#         # #head
#         # fill(random(255), random(255), random(255))
#         ellipse(circleH, 150, 150, 150)
        
#         # #left leg
#         # fill(random(255), random(255), random(255))
#         ellipse(circleLL - 75, 500, 100, 100)
        
#         # #right arm
#         # fill(random(255), random(255), random(255))
#         ellipse(circleRA + 75, 500, 100, 100)
        
#         # #left arm
#         # fill(random(255), random(255), random(255))
#         ellipse(circleLA - 120, 300, 75, 75)
        
#         # #right arm
#         # fill(random(255), random(255), random(255))
#         ellipse(circleRA + 120, 300, 75, 75)


#     # #eyes
#     fill(0)
#     ellipse((width/2 - 25), 130, 30, 30) #left eye
#     ellipse((width/2 + 25), 130, 30, 30) #right eye
#     ellipse((width/2), 180, 40, 10) #mouth

# Global color variable for left leg

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

colorH = (random(255), random(255), random(255))

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
    global colorH

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
