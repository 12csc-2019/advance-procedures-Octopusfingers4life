#importing tkinter so that i can create the GUI
from tkinter import *
from tkinter.filedialog import askopenfilename
#importing vlc so that i can play the music
import vlc

#creating global variables so that i can call them across functions
buttonPos = 5
fileDir = 'default'
song = 'default'

#creating the main class for the music player
class musicPlayer(Frame):
    

    
    def __init__(self):
        super().__init__()

        self.uiMaker()

    
    
    def uiMaker(self):
            
                   
        #creating the command for the exit button
        def programQuit():
            quit()

        #crating the command for the select song
        def addSong():
            global buttonPos
            global fileDir
            #opening a file explorer to get the user to select a song
            fileDir = askopenfilename()
            #splitting the file directory name at every / and storing it in a list
            fileSplit = fileDir.rsplit('/')
            #getting the length of the 'file dir' list 
            fileLength = len(fileSplit)
            #subtracting one of file length to get the file name
            fileLength = fileLength - 1
            #storing the file name in a variable
            songName = fileSplit[fileLength]
            #creating, drawing and moveing the button that displays the file name
            savedSong = Button(text = songName, bg = 'black', fg = 'white', command = startSong)
            savedSong.pack()
            savedSong.place(x = 200, y = buttonPos)
            #updating buttonPos to stop button overlaping
            buttonPos = buttonPos + 23
            

        #creating the function that starts the song
        def startSong():
            #calling global variables
            global fileDir
            global song
            #setting the media player variable to the song directory
            song = vlc.MediaPlayer(fileDir)
            #starting the song
            song.play()

        #creating the function the pauses the song
        def pauseMusic(): 
            #calling the global variable
            global song  
            #pausing the song
            song.pause()
            

        def playMusic():
            #calling the global vars
            global song
            #playing the song
            song.play()

        #deffining the text and command of the exit button
        exitButton = Button(text='X', bg = 'black', fg = 'white', command = programQuit)
        #drawing the exit button
        exitButton.pack()
        #moving the exit button to the correct position
        exitButton.place(x = 980, y = 5)

        #deffining the text and command of the select song button
        selectSong  = Button(text='Add a song', bg = 'black', fg = 'white', command = addSong)
        #drawing the select song button
        selectSong.pack()
        #moving the select song button to the correct position
        selectSong.place(x = 2, y = 5)

        #deffining the text and command of the pause button
        pauseButton = Button(text='||', bg = 'black', fg = 'white', command = pauseMusic)
        #drawing the pause button
        pauseButton.pack()
        #moving the exit button to the pause position
        pauseButton.place(x = 775, y = 470)

        #deffining the text and command of the select play button
        playButton = Button(text = "▶", bg = 'black', fg = 'white', command = song)
        #drawing the play button
        playButton.pack()
        #moving the play button to the correct position
        playButton.place(x = 750, y = 470)

        #setting the GUI name 
        self.master.title("Music player")
        self.pack(fill=BOTH, expand=1)
        
        #drawing the boxes on to the GUI
        canvas = Canvas(self)
        songPanel = canvas.create_rectangle(500, 5, 1.5, 497)
        musicInfo = canvas.create_rectangle(500, 5, 997, 370)
        musicControl = canvas.create_rectangle(500, 370, 997, 497)
        canvas.pack(fill=BOTH, expand=1)

        



def mainWindow():
    main = Tk()
    ex = musicPlayer()
    #setting the size of the window
    main.geometry('1000x500')
    main.mainloop()


#starting the loop
if __name__ == '__main__':
    mainWindow()


