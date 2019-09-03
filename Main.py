#importing required modules
import time
from graphics import *

win = GraphWin('Music player', 800, 400) # setting up the graphics window
defaultPoint = Point(0, 0) #creating the default point for my items

#making the window that will hold the music selector
selector = Rectangle(Point(350, 399), defaultPoint)
selector.setOutline('black')

selector.draw(win)

#making the window that will hold the music control
musicControl = Rectangle(Point(449, 120), defaultPoint)
musicControl.move(350, 279)
musicControl.setOutline('black')
musicControl.draw(win)

#making the window that will hold the info on music
musicInfo = Rectangle(Point(449, 279), defaultPoint)
musicInfo.move(350, 0)
musicInfo.setOutline('black')
musicInfo.draw(win)

selectMessage = Text(Point(0, 0), 'Click here to play a song')
selectMessage.move(180, 190)
selectMessage.draw(win)

testMessage = Text(Point(0, 0), 'Place holder for the ')

win.getMouse()
win.close()
