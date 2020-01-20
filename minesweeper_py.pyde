import os, random
path = os.getcwd()

#creating Tile class
#row,column
#value (number, mine or an empty tile: 'mine' |0 empty | 1-8)
#status (revealed: True | hidden: False ) 
#image
class Tile:
    def __init__(self,row,column,value,status):
        self.row=row
        self.column=column
        self.value=0 #empty tile
        self.status=False
     
        #loading images of a bomb, tile and a gameover image
        self.imgTile=loadImage(path+'/images/tile.png')
        self.imgMine=loadImage(path+'/images/mine.png')
        
    #displaying the numerical value of tiles
    def display(self):
            self.imgNum=loadImage(path+'/images/'+str(self.value)+'.png')
            #setting the variable for numbers
            if self.status==False: 
                #it means we display the tile image, since the tile is hidden
                image(self.imgTile, self.row*600/game.Rows, self.column*600/game.Columns,600/game.Rows,600/game.Columns)
            else:
                image(self.imgNum, self.row*600/game.Rows, self.column*600/game.Columns,600/game.Rows,600/game.Columns)
              

#defining game set up
class Minesweeper:
    def __init__(self):
        self.Rows=10
        self.Columns=10
        self.Bombs=10
        self.End=False
        self.gameover = False
        self.imgEnd=loadImage(path+'/images/gameover.png')
        self.imgWin=loadImage(path+'/images/win.png')
        self.revealed=self.Rows*self.Columns-self.Bombs
    
        #creating the set of neighbour tiles
        self.neighbours= [[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1]]
        
        #cretating the playing board
        self.board = []
        for r in range(self.Rows):
            for c in range(self.Columns):
                self.board.append(Tile(r,c,0,False))
        
        #randomly distributing bombs
        #after choosing a tile from the board to be the bomb, we change its value
        for tile in range(self.Bombs):
            tile=random.choice(self.board)
            tile.value='mine'
        
       #loop goes over the tiles until it finds a bomb
        for tile in self.board:
            #if there is a bomb. the loops goes over all the neighbours to increase the numerical value, except if the neighbour is also a bomb
            if tile.value=='mine': 
                for n in self.neighbours: 
                    newTile=self.getTile(tile.row + n[0], tile.column + n[1])
                    if newTile!=False and newTile.value!='mine':
                        newTile.value+=1
                         
                         
    def getTile(self,row,column):
        for tile in self.board:
            if tile.row==row and tile.column==column:
                return tile
        return False
    
    #defining the way to end the game|when the user finds the bomb
    def gameOver(self):
        for tile in self.board:
            if tile.value=='mine':
                tile.status=True
        self.End=True
    
    #opening all the empty tiles by repeating the process of looking for bombs
    def recursion(self,tile):
        tile.status = True
        for n in self.neighbours: 
            newTile=self.getTile(tile.row+n[0],tile.column+n[1])
            if newTile!=False:
                #if the tile is empty and the neighbour tile is hidden
                if newTile.value==0 and newTile.status==False:
                    self.recursion(newTile)
                if newTile.value!='mine':
                    newTile.status=True
    
    def clicked(self):
        #print('clicked')
        if self.End==False:
            row=mouseX//(600//self.Columns)
            column=mouseY//(600//self.Rows)
            tile=self.getTile(row,column)
            
            #if the tile is a bomb the game is over
            if tile.value=='mine':
                tile.status=True
                image(self.imgEnd,0,0,500,500)
                self.gameOver()
                return
           
             #if it is an empty tile, recursion occures and all empty neigbours are opened
            if tile.value == 0:
                self.recursion(tile)
            tile.status = True
        
        #checking if there is a win 
        #if there is the same number of bombs and unrevealed tiles, the player won the game
        cnt=0
        for t in self.board:
            if t.status==True and t.value!='mine':
                cnt+=1
        #print(cnt, self.revealed)
        if cnt==self.revealed:
            self.gameover=True
            for tile in self.board:
                if tile.value == 'mine':
                    tile.status=True
            
    def display(self):
        for tile in self.board:
            tile.display()
        if self.gameover:
            image(self.imgWin,0,0,500,500)
            
game=Minesweeper()

def setup():
    size(600,600)
    
def draw():
    game.display()
    
def mouseClicked():
    game.clicked()
                
