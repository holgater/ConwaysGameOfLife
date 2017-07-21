from graphics import *
from variables import *

win = GraphWin('Board', (BOARD_SIZE*(500/BOARD_SIZE))+100, (BOARD_SIZE*(500/BOARD_SIZE)))

Board_G = [[Rectangle(Point(0,0),Point(0,0))]*BOARD_SIZE for _ in range(BOARD_SIZE)]

speedText = Text(Point(550,30), "Speed")
speedText.draw(win)

speedBox = Entry(Point(550,60), 10)
speedBox.setText(SPEED)
speedBox.draw(win)
