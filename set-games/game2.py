





class Target(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def if_collapse(self):
        check = False
        if (self.x - self.y) <= 0:
            check = True
        return check


class JumpingGame(object):


    
    def __init__(self, player_one, player_two, health, grid_x, grid_y):
        self.player_one = player_one
        self.player_two = player_two 
        self.health = health
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.mat1 = []
        self.mat2 = [] 
        
        
    def startGame(self, x, y):
        matching = 0
        self.displayGame()
        t = Target(pow(x, 2), pow(y, 2)) 
        
        endGame = False

        if t.if_collapse():
            endGame = True
        
    
        for i in range(0, (x + y)):
            self.mat1[i] = t.getX() + 1
            self.mat2[i] = t.getX() - 1
            if self.mat1[i] == self.mat2[i]:
                matching += 1
            else:
                matching -= 1
                
        if matching == 0:
            endGame = True
        

        return endGame
                
        
        

    def displayGame(self):
    
        for i in range(0, self.grid_x):
            for j in range(0, self.grid_y):
                self.mat1.append(i * j)
            self.mat2.append(self.mat1)

        print(self.mat2) 
    


grid_input_one = int(input("x coordinate: "))
grid_input_two = int(input("y coordinate: "))




game = JumpingGame('X','Y', 100, grid_input_one, grid_input_two)



while True:
    game.displayGame()
    player_one = int(input("X Attack: "))
    player_two = int(input("Y Attack: "))
    if player_one <= 0:
        print("try again, should be positive number attack for X") 
        continue
    if player_two <= 0:
        print("try again, should be positive number attack for Y") 
        continue 
    if (game.startGame(player_one, player_two)):
        print("Game Over") 
        break 

        
