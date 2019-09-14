from tkinter import *
from tkinter.filedialog import askopenfilename

from playsound import playsound

class musicPlayer(Frame):

    
    def __init__(self):
        super().__init__()

        self.uiMaker()
    
    def uiMaker(self):
        def playMusic():
            fileName = askopenfilename(filetypes=[("Music files", "*.mp3")])
            playsound(fileName)

        
        self.master.title("Music player")
        self.pack(fill=BOTH, expand=1)
        
        canvas = Canvas(self)
        selectSong = canvas.create_rectangle(500, 5, 1.5, 497)
        musicInfo = canvas.create_rectangle(500, 5, 997, 370)
        musicControl = canvas.create_rectangle(500, 370, 997, 497)
        canvas.pack(fill=BOTH, expand=1)

        playMusic = Button(text="play music",bg = 'black', fg = 'white',command = playMusic)
        playMusic.pack()
        playMusic.place(x = 250, y = 248.5)

def mainWindow():
    main = Tk()
    ex = musicPlayer()
    main.geometry('1000x500')
    main.mainloop()



if __name__ == '__main__':
    mainWindow()


