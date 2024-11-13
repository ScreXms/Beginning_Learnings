'''
Victoria Duong
Toolkit-Python.A.Fa24
Code Assignment #5: One Button Game
2024.10.23
'''

switchChange = True

def setup():
    size(600, 600)
    noStroke()
    frameRate(5)
    
def draw():
    background(30, 30, 30)
    
    draw_circle(width/2, 350, 300) #tummy
    draw_circle(width/2, 150, 150) #head
    draw_circle((width/2 - 75), 500, 100) #left leg
    draw_circle((width/2 + 75), 500, 100) #right leg
    draw_circle((width/2 - 120), 300, 75) #left arm
    draw_circle((width/2 + 120), 300, 75) #right arm
    
    fill(255)
    ellipse((width/2 - 25), 120, 30, 30) #left eye
    ellipse((width/2 + 25), 120, 30, 30) #right eye
 
def draw_circle(x, y, size): 
        r = random(0, 255)
        g = random(0, 255)
        b = random(0, 255)
                    
        fill(r, g, b)
        ellipse(x, y, size, size)
        
def keyPressed():
    global switchChange
    if key == ' ':
        switchChange = False
        fill("#FF0509")
        
def keyReleased():
    global switchChange
    if key == ' ':
        switchChange = True


# switchChange = True
# stored_colors = {}  # Dictionary to store current colors when space bar is pressed

# def setup():
#     size(600, 600)
#     noStroke()
#     frameRate(5)

# def draw():
#     background(30, 30, 30)
    
#     # Draw character parts with stored or generated colors
#     draw_circle("tummy", width / 2, 350, 300)
#     draw_circle("head", width / 2, 150, 150)
#     draw_circle("left_leg", width / 2 - 75, 500, 100)
#     draw_circle("right_leg", width / 2 + 75, 500, 100)
#     draw_circle("left_arm", width / 2 - 120, 300, 75)
#     draw_circle("right_arm", width / 2 + 120, 300, 75)

#     # Draw the eyes (fixed white color)
#     fill(255)
#     ellipse(width / 2 - 25, 120, 30, 30)  # Left eye
#     ellipse(width / 2 + 25, 120, 30, 30)  # Right eye

# def draw_circle(part, x, y, size):
#     global stored_colors
    
#     if switchChange:
#         # Generate random colors if switchChange is True
#         r, g, b = random(0, 255), random(0, 255), random(0, 255)
#         stored_colors[part] = (r, g, b)  # Store the colors when switchChange is True
#     else:
#         # Use the stored color if switchChange is False
#         r, g, b = stored_colors.get(part, (200, 200, 200))  # Default to gray if color isn't set

#     fill(r, g, b)
#     ellipse(x, y, size, size)

# def keyPressed():
#     global switchChange
#     if key == ' ':
#         switchChange = False  # Freeze the colors when the space bar is pressed

# def keyReleased():
#     global switchChange
#     if key == ' ':
#         switchChange = True  # Resume changing colors when space bar is released


    
