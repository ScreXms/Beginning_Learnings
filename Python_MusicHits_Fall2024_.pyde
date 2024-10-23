

musicnote = loadImage ("Gold_MusicNote.png") #4096 x 4096

songTitles = [ 
    "Tik Tok by Kesha", 
    "Need You Now by Lady Antebellum", 
    "Hey, Soul Sister by Train", 
    "California Gurls by kay Perry featuring Snoop Dogg",
    "OMG by Usher featuring will.i.am"
    # "Airplanes by B.o.B featuring Hayley Williams",
    # "Love the Way You Lie by Eminem featuring Rihanna",
    # "Bad Romance by lady Gaga", 
    # "Dynamite by Taio Cruz",
]
ranking = [
    100,
    150,
    200,
    250,
    300,
    350,
]

currentSong = 0 #track current song
changeInterval = 1500 #1.5 seconds
lastChange = 0 # store the last change time

def setup():
    global musicnote
    size(1200, 600)
    musicnote = loadImage ("Gold_MusicNote.png") #4096 x 4096
    f = createFont("Bernard MT Condensed", 40)
    textFont(f)
    # printArray(PFont.list())
    
def draw(): 
    global musicnote, currentSong, lastChange
    
    background(0)
    if musicnote: 
        image(musicnote, 50, 100, 4096/10, 4096/10)
    textAlign(CENTER)
    fill(255, 215, 0)
    
    if millis() - lastChange > changeInterval: # lastchange = holds timestamp of last time the song title changed 
        currentSong = (currentSong + 1) % len(songTitles) # updates / len(songTitles) = all songs in list
        lastChange = millis() #update last change time
    text(songTitles[currentSong], width/2, 100)

# bars
    i = 400 # start of bars
    # for j in range(len(ranking)): # loop thro each ranking
    # while i <= mouseX:
    #     c = map(i, 100, width, 30, 255) # i map based on i (x position)
    fill(255, 215, 0, 100) # (red, green, blue, transparency
    rect(i, 125, 50, ranking[currentSong]) # (x, y, width, height)
        # i += 100 # increment of x position for next bar
