from graphics import *
import time

BOARD_SIZE = 10
SPEED = 25
TIME = SPEED
Board_1 = [[False]*BOARD_SIZE for _ in range(BOARD_SIZE)]
Board_2 = [[False]*BOARD_SIZE for _ in range(BOARD_SIZE)]

win = GraphWin('Board', (BOARD_SIZE*(500/BOARD_SIZE))+100, (BOARD_SIZE*(500/BOARD_SIZE)))

Board_G = [[Rectangle(Point(0,0),Point(0,0))]*BOARD_SIZE for _ in range(BOARD_SIZE)]

speedText = Text(Point(550,30), "Speed")
speedText.draw(win)

speedBox = Entry(Point(550,60), 10)
speedBox.setText(SPEED)
speedBox.draw(win)

def Set(c,r):
    neighbor_count = Get_Count(c,r)
    if neighbor_count < 2:
        return False
    if neighbor_count == 2:
        return Board_1[c][r]
    if neighbor_count == 3:
        return True
    if neighbor_count > 3:
        return False

def Get_Count(c,r):
    count = 0
    for i in range(3):
        for j in range(3):
            board_c = c-1+j
            board_r = r-1+i
            if (board_c >= 0 and board_r >= 0 and board_c < BOARD_SIZE and board_r < BOARD_SIZE):
                if Board_1[board_c][board_r]:
                    count += 1
    if Board_1[c][r]:
        count -= 1
    return count

def Print_Board(board):
    global Board_G
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            tile = Rectangle(Point((c*50),(r*50)),Point(((c+1)*50),((r+1)*50)))
            if board[c][r]:
                tile.setFill("black")
            else:  
                tile.setFill("white")
                tile.setOutline("black")
            prev_tile = Board_G[c][r]
            tile.draw(win)
            Board_G[c][r] = tile
            prev_tile.undraw()
    win.flush()

def Get_Click():
    clickPoint = win.checkMouse()
    if(clickPoint != None):
        clickTile = Point((clickPoint.getX()-25)/50, (clickPoint.getY()-25)/50)
        c = round(clickTile.getX())
        r = round(clickTile.getY())
        Board_1[c][r] = not(Board_1[c][r])
        Print_Board(Board_1)

def Update_Speed():
    global SPEED
    global TIME
    if speedBox.getText() == "":
        SPEED = 1
    elif speedBox.getText() == "0":
        SPEED = 1
    else:
        SPEED = speedBox.getText() 
    if TIME > int(SPEED):
        TIME = 0
    win.flush()

def Tick():
    global TIME
    TIME += 1
    time.sleep(0.01)
    if TIME > int(SPEED):
        TIME = 0
        return True

while(1):
    if Tick():
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                Board_2[c][r] = Set(c,r)
        Board_1 = Board_2
        Board_2 = [[False]*BOARD_SIZE for _ in range(BOARD_SIZE)]
        Print_Board(Board_1)
    Get_Click()
    Update_Speed()
win.close()
