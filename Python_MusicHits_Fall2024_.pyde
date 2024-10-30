

musicnote = loadImage ("Gold_MusicNote.png") #4096 x 4096

songTitles = [ 
    "Tik Tok by Kesha", #1
    "Need You Now by Lady Antebellum", #2
    "Hey, Soul Sister by Train", #3
    "California Gurls by Katy Perry ft. Snoop Dogg", #4
    "OMG by Usher ft. Will.i.am", #5
    "Airplanes by B.o.B ft. Hayley Williams", #6
    "Love the Way You Lie by Eminem ft. Rihanna", #7
    "Bad Romance by Lady Gaga", #8
    "Dynamite by Taio Cruz", #9
    "Break Your Heart by Taio Cruz ft. Ludacris", #10
    "Nothin' on You by B.o.B ft. Bruno Mars", #11
    "I Like It by Enrique Iglesias ft. Pitball" #12
    "BedRock by Young Money ft. Lloyd", #13
    "In My Head by Jason Derulo" #14
    "Rude Boy by Rihanna", #15
    "Telephone by Lady Gaga ft. Beyonce", #16
    "Teenage Dream by Katy Perry", #17
    "Just the Way You Are by Bruno Mars", #18
    "Cooler Than Me by Mike Posner", #19
    "Imma Be by The Black Eyed Peas", #20
    "Empire State of Mind by Jay-Z ft. Alicia Keys", #21
    "DJ Got US FAllin' in Love by Usher ft. Pitball", #22
    "Billionaire by Travie McCoy ft. Bruno Mars", #23
    "Not Afraid by Eminem", #24
    "Replay by Iyaz" #25
    "Secy Bitch by David Guetta ft. Akon", #26
    "Breakeven by The Script", #27
    "Your Love Is my Drug by Kesha", #28
    "I gotta Feeling by The Black Eyed Peas", #29
    "Fireflies by Owl City", #30
    "Say Aah by Trey Songz ft. Fabolous", #31
    "Find Your Love by Drake", #32
    "Alejandro by Lady Gaga", #33
    "Ridin' Solo by Jason Derulo", #34
    "Just a Dream by Nelly", #35
    "Like a G6 by Far East Movement ft. The Cataracs and Dev", #37
    "Carry Out by Timbaland ft. Justin Timerlake", #38
    "Haven't Met You Yet by Michael Buble", #39
    "Club Can't Handle Me by Flo Rida ft. David Guetta", #40
    "Down by Jay Sean ft. Lil Wayne", #41
    "Bulletproof by La Roux", #42
    "Whatcha Say by Jason Derulo", #43
    "Baby by Justin Bieber ft. Ludacris", #44
    "Whataya Want from Me by Adam Lambert", #45
    "Mine by Taylor Swift", #46
    "Only Girl(In the World) by Rihanna", #47
    "Like Like We're Dying by Kris Allen", #48
    "Hard by Rihanna ft. Jeezy", #49
    "Young Forver by Jay-Z ft. Mr Hudson" #50
]
ranking = [
    15, #1
    30, #2
    45, #3
    60, #4
    75, #5
    90, #6
    105, #7
    120, #8
    135, #9
    150, #10
    165, #11
    180, #12
    195, #13
    210, #14
    225, #15
    240, #16
    255, #17
    270, #18
    285, #19
    300, #20
    315, #21
    330, #22
    345, #23
    360, #24
    375, #25
    390, #26
    405, #27
    420, #28
    435, #29
    450, #30
    465, #31
    480, #32
    495, #33
    510, #34
    525, #35
    540, #36
    555, #37
    570, #38
    585, #39
    600, #40
    615, #41
    630, #42
    645, #43
    660, #44
    675, #45
    690, #46
    705, #47
    720, #48
    735, #49
    750, #50
]

currentSong = 0 #track current song
changeInterval = 1000 #1 seconds
lastChange = 0 # store the last change time
i = 345 # initialize 'i' outside the draw to keep its value across every frame

def setup():
    global musicnote
    size(1500, 1000)
    musicnote = loadImage ("Gold_MusicNote.png") #4096 x 4096
    f = createFont("Bernard MT Condensed", 40)
    textFont(f)
    # printArray(PFont.list())
    
def draw(): 
    global musicnote, currentSong, lastChange, i
    
    background(0)
    if musicnote: 
        image(musicnote, 0, 250, 4096/10, 4096/10)
    textAlign(CENTER)
    fill(255, 215, 0)
    
    if millis() - lastChange > changeInterval: # lastchange = holds timestamp of last time the song title changed 
        currentSong = (currentSong + 1) % len(songTitles) # updates / len(songTitles) = all songs in list
        lastChange = millis() #update last change time
        
        if currentSong == 0:
            i = 345
        else: 
            i += 25
    
    text(songTitles[currentSong], width/2, 100)
    
# bars

    fill(255, 215, 0, 100)
    rect(i, 125, 25, ranking[currentSong]) #(x, y, width, height)
