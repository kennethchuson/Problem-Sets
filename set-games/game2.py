





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
    def __init_(self, player, health, grid_x, grid_y):
        self.player = player
        self.health = health
        self.grid_x = grid_x
        self.grid_y = grid_y

    def Menu(self, choose):
        if choose == 1:
            self.startGame() 
        elif choose == 2:
            self.endGame() 
        else:
            raise Exception("No options!")
        
    def startGame(self):
        self.displayGame() 
        

    def displayGame(self):
        mat1 = []
        mat2 = [] 
        for i in range(0, self.grid_x):
            for j in range(0, self.grid_y):
                mat1.append([i, j])
            mat2.append(mat1)
        print(mat2)


grid_input_one = int(input("x coordinate: "))
grid_input_two = int(input("y coordinate: "))

t_input_one_x = int(input("target 1: "))
t_input_two_y = int(input("target 2: "))


game_player_one = JumpingGame('X', 100, grid_input_one, grid_input_two)
game_player_two = JumpingGame('Y', 100, grid_input_one, grid_input_two)

game_player_one.displayGame()


        
