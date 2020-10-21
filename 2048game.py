
from graphics import *
from random import *


class game:
    drawinglist = []
    fontsize = 36
    cordinatelist =[[(175,175),(325,175),(475,175),(625,175)],
                    [(175,325),(325,325),(475,325),(625,325)],
                    [(175,475),(325,475),(475,475),(625,475)],
                    [(175,625),(325,625),(475,625),(625,625)]
                    ]
    cordinatepoistion = {(0,0):(175,175),(0,1):(325,175),(0,2):(475,175),(0,3):(625,175),
        (1,0):(175,325),(1,1):(325,325),(1,2):(475,325),(1,3):(625,325),
        (2,0):(175,475),(2,1):(325,475),(2,2):(475,475),(2,3):(625,475),
        (3,0):(175,625),(3,1):(325,625),(3,2):(475,625),(3,3):(625,625)
        }
    controls ={'w':'up','s':'down','a':'left','d':'right'}

    # horizontal line 
    pointA = Point(100,100)
    pointB = Point(700,100)
    pointC = Point(100,700)
    pointD = Point(700,700)
    pointE = Point(100,250)
    pointF = Point(100,400)
    pointG = Point(100,550)
    pointH = Point(700,250)
    pointI = Point(700,400)
    pointJ = Point(700,550)

    line1 = Line(pointA,pointB)
    line2 = Line(pointE,pointH)
    line3 = Line(pointF,pointI)
    line4 = Line(pointG,pointJ)
    line5 = Line(pointC,pointD)

    line6 = Line(Point(100,100),Point(100,700))
    line7 = Line(Point(250,100),Point(250,700))
    line8 = Line(Point(400,100),Point(400,700))
    line9 = Line(Point(550,100),Point(550,700))
    line10 = Line(Point(700,100),Point(700,700))


    def __init__(self):
        self.newgame()

    def newgame(self):
        self.tilelist =[[],[],[],[]]
        for i in range(4):
            for x in range(4):
                newtitle = tile()
                newtitle.x_cord = self.cordinatelist[i][x][0]
                newtitle.y_cord = self.cordinatelist[i][x][1]
                self.tilelist[i].append(newtitle)
    
        self.generate_two_position()
        self.gamepad()
 

    def generate_two_position(self): # generate 2 random cordinates for two 2s in the gameborad
        position1_x = randint(0,3)
        position1_y = randint(0,3)
        random_position1 = self.cordinatepoistion[(position1_x,position1_y)]
        position2_x = randint(0,3)
        position2_y = randint(0,3)
        random_position2 = self.cordinatepoistion[(position2_x,position2_y)]

        while random_position1 == random_position2:
            position2_x = randint(0,3)
            position2_y = randint(0,3)
            random_position2 = self.cordinatepoistion[(position2_x,position2_y)] # make sure two positions not be the same
        
        self.tilelist[position1_x][position1_y].x_cord = random_position1[0]
        self.tilelist[position1_x][position1_y].y_cord = random_position1[1]
        self.tilelist[position1_x][position1_y].value = '2'
        self.tilelist[position2_x][position2_y].x_cord = random_position2[0]
        self.tilelist[position2_x][position2_y].y_cord = random_position2[1]
        self.tilelist[position2_x][position2_y].value = '2'

        self.message1 = Text(Point(random_position1[0],random_position1[1]),'2')
        self.message1.setSize(game.fontsize)
        self.drawinglist.append(self.message1)
        self.message2 = Text(Point(random_position2[0],random_position2[1]),'2')
        self.message2.setSize(game.fontsize)
        self.drawinglist.append(self.message2)

    def gamepad(self):
        global win
        global rectScore
        global rectHighestScore
        global rectmenuQuit
        global rectmenuRestart
        global score
        global highestscore

        win = GraphWin('2048 Game',800,800,autoflush=False)
        rectScore = Rectangle(Point(300,20),Point(380,40))
        centerpointsS = rectScore.getCenter()
        score = Text(centerpointsS,0)
        score.draw(win)

        scoreText = Text(Point(280,30),'Score')
        scoreText.draw(win)


        # menu
        rectmenuQuit = Rectangle(Point(700,20),Point(780,40))
        rectmenuRestart = Rectangle(Point(700,60),Point(780,80))
        rectmenuQuit.draw(win)
        rectmenuRestart.draw(win)
        middelpoistionQuit = rectmenuQuit.getCenter()
        middelpoistionRestart = rectmenuRestart.getCenter()
        QuitText = Text(middelpoistionQuit,'Quit')
        QuitText.setStyle('bold')
        RestartText = Text(middelpoistionRestart,'Restart')
        RestartText.setStyle('bold')
        QuitText.draw(win)
        RestartText.draw(win)
        
        rectScore.draw(win)
        game.line1.setWidth(5)
        game.line2.setWidth(5)
        game.line3.setWidth(5)
        game.line4.setWidth(5)
        game.line5.setWidth(5)
        game.line6.setWidth(5)
        game.line7.setWidth(5)
        game.line8.setWidth(5)
        game.line9.setWidth(5)
        game.line10.setWidth(5)


        game.line1.draw(win)
        game.line2.draw(win)
        game.line3.draw(win)
        game.line4.draw(win)
        game.line5.draw(win)
        game.line6.draw(win)
        game.line7.draw(win)
        game.line8.draw(win)
        game.line9.draw(win)
        game.line10.draw(win)
        self.message1.draw(win)
        self.message2.draw(win)

        self.getUserAction()
        win.getMouse()


    def getUserAction(self):
        while True:
            action = win.getKey()
            if action in game.controls:
                self.Move(action)
            

    def Move(self,action):
        shift = 0
        if action.upper() == 'S':
            for j in range(0,4):
                shift = 0
                for i in range(3,-1,-1):
                    if self.tilelist[i][j].value == '':
                        shift += 1
                    else:
                        if i -1 >= 0 and self.tilelist[i-1][j].value == self.tilelist[i][j].value:
                            self.tilelist[i][j].value = str(int(self.tilelist[i][j].value)*2)
                            currentscore = score.getText()
                            newscore = int(currentscore) + int(self.tilelist[i][j].value)
                            score.setText(newscore)
                            self.tilelist[i-1][j].value = ''
                        elif i -2 >= 0 and self.tilelist[i-1][j].value == '' and self.tilelist[i-2][j].value == self.tilelist[i][j].value:
                            self.tilelist[i][j].value = str(int(self.tilelist[i][j].value)*2)
                            currentscore = score.getText()
                            newscore = int(currentscore) + int(self.tilelist[i][j].value)
                            score.setText(newscore)
                        elif i == 3 and (self.tilelist[2][j].value =='' and self.tilelist[1][j].value =='') and self.tilelist[0][j].value == self.tilelist[3][j].value:
                            self.tilelist[3][j].value = str(int(self.tilelist[3][j].value)*2)
                            currentscore = score.getText()
                            newscore = int(currentscore) + int(self.tilelist[3][j].value)
                            score.setText(newscore)
                            self.tilelist[0][j].value = ''
                        if shift > 0:
                            self.tilelist[i+shift][j].value = self.tilelist[i][j].value
                            self.tilelist[i][j].value = ''
            self.print_gamepad(self.tilelist)
            self.generate_new_number()
            status = self.gamecheck() # check whether the game is over or win
            if status == True:
                self.gamelose()


        if action.upper() == 'A':
            for i in range(0,4):
                shift = 0
                for j in range(0,4):
                    if self.tilelist[i][j].value == '':
                        shift += 1
                    else:
                        if j + 1 < 4 and self.tilelist[i][j+1].value == self.tilelist[i][j].value:
                            self.tilelist[i][j].value = str(int(self.tilelist[i][j].value)*2)
                            currentscore = score.getText()
                            newscore = int(currentscore) + int(self.tilelist[i][j].value)
                            score.setText(newscore)

                            self.tilelist[i][j+1].value = ''
                        elif j +2 < 4 and self.tilelist[i][j+1].value == '' and self.tilelist[i][j+2].value==self.tilelist[i][j].value:
                            self.tilelist[i][j].value = str(int(self.tilelist[i][j].value)*2)
                            currentscore = score.getText()
                            newscore = int(currentscore) + int(self.tilelist[i][j].value)
                            score.setText(newscore)
                            self.tilelist[i][j+2].value = ''

                        elif j == 0 and (self.tilelist[i][1].value == '' and self.tilelist[i][2].value == '') and self.tilelist[i][3] == self.tilelist[i][0]:
                            self.tilelist[i][0].value = str(int(self.tilelist[i][0].value)*2)
                            currentscore = score.getText()
                            newscore = int(currentscore) + int(self.tilelist[i][0].value)
                            score.setText(newscore)
                            self.tilelist[i][3].value = ''

                        if shift > 0:
                            self.tilelist[i][j-shift].value = self.tilelist[i][j].value
                            self.tilelist[i][j].value = ''

            self.print_gamepad(self.tilelist)
            self.generate_new_number()
            status = self.gamecheck()
            if status == True:
                self.gamelose()

                   


        if action.upper() == 'W':
            for j in range(0,4):
                shift = 0
                for i in range(0,4):
                    if self.tilelist[i][j].value == '':
                        shift += 1
                    else:
                        if i + 1< 4 and self.tilelist[i+1][j].value == self.tilelist[i][j].value:
                            self.tilelist[i][j].value = str(int(self.tilelist[i][j].value)*2)
                            currentscore = score.getText()
                            newscore = int(currentscore) + int(self.tilelist[i][j].value)
                            score.setText(newscore)
                            self.tilelist[i+1][j].value = ''
                        elif i + 2 < 4 and self.tilelist[i+1][j].value == 0 and self.tilelist[i+2][j].value == self.tilelist[i][j].value:
                            self.tilelist[i][j].value = str(int(self.tilelist[i][j].value)*2)
                            currentscore = score.getText()
                            newscore = int(currentscore) + int(self.tilelist[i][j].value)
                            score.setText(newscore)
                            self.tilelist[i+2][j].value = ''
                        elif i == 0 and (self.tilelist[1][j].value and self.tilelist[2][j].value == '') and self.tilelist[3][j].value == self.tilelist[0][j].value:
                            self.tilelist[0][j].value = str(int(self.tilelist[0][j].value)*2)
                            currentscore = score.getText()
                            newscore = int(currentscore) + int(self.tilelist[0][j].value)
                            score.setText(newscore)
                        if shift > 0:
                            self.tilelist[i-shift][j].value = self.tilelist[i][j].value
                            self.tilelist[i][j].value = ''
            self.print_gamepad(self.tilelist)
            self.generate_new_number()
            status = self.gamecheck()
            if status == True:
                self.gamelose()



        if action.upper() == 'D':
            for i in range(0,4):
                shift = 0
                for j in range(3,-1,-1):
                    if self.tilelist[i][j].value =='':
                        shift += 1
                    else:
                        if j -1 >= 0 and self.tilelist[i][j-1].value == self.tilelist[i][j].value:
                            self.tilelist[i][j].value = str(int(self.tilelist[i][j].value)*2)
                            currentscore = score.getText()
                            newscore = int(currentscore) + int(self.tilelist[i][j].value)
                            score.setText(newscore)
                            self.tilelist[i][j-1].value = ''
                        elif j - 2 >= 0 and self.tilelist[i][j-1].value == '' and self.tilelist[i][j-2].value == self.tilelist[i][j].value:
                            self.tilelist[i][j].value = str(int(self.tilelist[i][j].value)*2)
                            currentscore = score.getText()
                            newscore = int(currentscore) + int(self.tilelist[i][j].value)
                            score.setText(newscore)
                            self.tilelist[i][j-2].value = ''
                        elif j == 3 and (self.tilelist[i][2].value == '' and self.tilelist[i][1].value == '') and self.tilelist[0][j].value == self.tilelist[3][j].value:
                            self.tilelist[i][3].value = str(int(self.tilelist[i][3].value)*2)
                            currentscore = score.getText()
                            newscore = int(currentscore) + int(self.tilelist[i][3].value)
                            score.setText(newscore)
                            self.tilelist[i][0].value = ''
                        if shift > 0:
                            self.tilelist[i][j+shift].value = self.tilelist[i][j].value
                            self.tilelist[i][j].value = ''
            self.print_gamepad(self.tilelist)
            self.generate_new_number()
            status = self.gamecheck()
            if status == True:
                self.gamelose()


        self.getUserAction()

        
    def print_gamepad(self,tilelist):
        # undraw all in the graph before redraw the graph after the move
        for drawingobject in self.drawinglist:
            drawingobject.undraw()

        for i in range(4):
            for x in range(4):
                outputtext = Text(Point(tilelist[i][x].x_cord,tilelist[i][x].y_cord),tilelist[i][x].value)
                outputtext.setSize(self.fontsize)
                self.drawinglist.append(outputtext)
                outputtext.draw(win)

    def gamecheck(self):
        for i in range(0,4):
            for x in range(0,4):
                if self.tilelist[i][x].value =='2048':
                    self.gamewin()
        for i in range(0,4):
            for x in range(0,4):
                if self.tilelist[i][x].value =='':
                    return False
        for i in range(0,4):
            for x in range(0,3):
                if (self.tilelist[i][x].value == self.tilelist[i][x+1].value):
                    return False
        for i in range(0,4):
            for x in range(0,3):
                if self.tilelist[x][i].value == self.tilelist[x+1][i].value:

                    return False
        return True
            
    def gamewin(self):
        congrats = Text(Point(50,50),'You won the Game !!')
        congrats.setStyle('bold')
        congrats.setSize(self.fontsize)
        congrats.draw(win)
        
        clickpoint = win.getMouse()
        if self.inside(clickpoint,rectmenuQuit):
            win.close()
        if self.inside(clickpoint,rectmenuRestart):
            win.close()
            self.newgame()

    def gamelose(self):
        lose = Text(Point(500,50),'Game Over')
        lose.setStyle('bold')
        lose.setSize(self.fontsize)
        lose.draw(win)
        while True:
            clickpoint = win.getMouse()
            if self.inside(clickpoint,rectmenuQuit):
                win.close()
            if self.inside(clickpoint,rectmenuRestart):
                win.close()
                self.newgame()

    def generate_new_number(self): # generate a 2 or 4 each slide been made, 67% being a 2, 33% being a 4
        twoORfourlist = ['2','2','4']
        index = randint(0,2)
        randomNumber = twoORfourlist[index]
        count = 0
        while True:
            count += 1
            randomplace_x = randint(0,3)
            randomplace_y = randint(0,3)
            randomposition = self.cordinatepoistion[(randomplace_x,randomplace_y)]
            if self.tilelist[randomplace_x][randomplace_y].value == '':
                self.tilelist[randomplace_x][randomplace_y].value = randomNumber
                self.tilelist[randomplace_x][randomplace_y].x_cord = randomposition[0]
                self.tilelist[randomplace_x][randomplace_y].y_cord = randomposition[1]
                message = Text(Point(randomposition[0],randomposition[1]),randomNumber)
                self.drawinglist.append(message)
                message.setSize(self.fontsize)
                message.draw(win)
                break
            elif count == 16:
                if self.status_check() == False:
                    text = Text(Point(100,80),'Game Over')
                break

    def status_check(self): 
        clickpoint = win.checkMouse()
        print(clickpoint)
        if self.inside(clickpoint,rectmenuQuit):
            return 'Game Quit'
        if self.inside(clickpoint,rectmenuRestart):
            return 'Restart'
    
    def inside(self,point,rectangle): # check whther clickpoint is inside the menu to quit or restart the game
        if point == None:
            return False
        ll = rectangle.getP1()
        ur = rectangle.getP2()
        return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

class tile:
    def __init__(self,x_cord = None,y_cord = None,value = ''):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.value = value


if __name__ =='__main__':
    game1 = game()



