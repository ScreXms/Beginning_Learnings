'''
Victoria Duong
Toolkit-Python.A.Fa.24
Code Assignment #4.b: Create a Endless animation using found objects
2024.10.15
'''

Baby = loadImage("Baby_Fist.png") #666*659
Grumpy = loadImage("Grumpy_Cat.png") #746*514
Meme = loadImage("Meme_Head.png") #316*316
Mike = loadImage("Mike.png") #656*651
Really = loadImage("Really_Cat.png") #699*708
Hide = loadImage("Hide_Bush.png") #636*638

def setup():
    size(1000, 1000)
    
    printArray(PFont.list())
    
    # f = createFont("Arial Narrow Bold", 40)
    textSize(40)
    fill(255)
    # stroke(0)
    textAlign(CENTER)
    frameRate(3)
    
    
def draw():
    background(0)
    text ("How I feel when I gotta do something I don't wanna", width/2, 100)
    
    image_choice = int(random(6))
    
    if image_choice == 0:
        image(Baby, 150, 200, 666, 659)
    if image_choice == 1:
        image(Grumpy, 150, 250, 746, 514)
    if image_choice == 2:
        image(Meme, 150, 200, 316 * 2, 316 * 2)    
    if image_choice == 3:
        image(Mike, 150, 200, 656, 651)
    if image_choice == 4:
        image(Really, 150, 200, 699, 708)
    if image_choice == 5:
        image(Hide, 150, 200, 636, 638)
