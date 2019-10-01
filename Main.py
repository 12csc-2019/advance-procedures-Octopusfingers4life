from tkinter import *
from tkinter.filedialog import askopenfilename

    
from pydub import AudioSegment
from pydub.playback import play



class musicPlayer(Frame):

    
    def __init__(self):
        super().__init__()

        self.uiMaker()
    
    def uiMaker(self):
        def selectMusic():
             songName = askopenfilename(filetypes=[("Music files", "*.mp3")])
             songDir = AudioSegment.from_mp3("test_sound.mp3")
             play(songDir)

        def programQuit():
            quit()

        def addSong():
            fileDir = askopenfilename()
            fileSplit = fileDir.rsplit('/')
            fileLength = len(fileSplit)
            fileLength = fileLength - 1
            songName = fileSplit[fileLength]
            savedSong = Button(text = songName, bg = 'black', fg = 'white')
            savedSong.pack()


              
        self.master.title("Music player")
        self.pack(fill=BOTH, expand=1)
        
        canvas = Canvas(self)
        songPanel = canvas.create_rectangle(500, 5, 1.5, 497)
        musicInfo = canvas.create_rectangle(500, 5, 997, 370)
        musicControl = canvas.create_rectangle(500, 370, 997, 497)
        canvas.pack(fill=BOTH, expand=1)

        playMusic = Button(text="play music",bg = 'black', fg = 'white', command = selectMusic)
        playMusic.pack()
        playMusic.place(x = 250, y = 248.5)

        exitButton = Button(text='X', bg = 'black', fg = 'white', command = programQuit)
        exitButton.pack()
        exitButton.place(x = 980, y = 5)

        selectSong  = Button(text='Add a song', bg = 'black', fg = 'white', command = addSong)
        selectSong.pack()
        selectSong.place(x = 2, y = 5)




def mainWindow():
    main = Tk()
    ex = musicPlayer()
    main.geometry('1000x500')
    main.mainloop()



if __name__ == '__main__':
    mainWindow()


