








class Target(object):
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.c = char

    def get_x(self):
        if self.x - self.y <= 0:
            self.x = abs(self.x) 
        return self.x
    
    def get_y(self):
        if self.y - self.x <= 0:
            self.y = abs(self.y) 
        return self.y

    def fill_target(self):
        if self.c == "":
            self.c = "X" 
        return self.c
    


class GamePad(object):

    
    def __init__(self, row, col): 
        self.row = row
        self.col = col
        self.mat1 = []
        self.mat2 = []

        
    def coordination_check(self):
        pad = [] 
        counter_x = 0
        counter_y = 0
        for i in range(len(self.mat2)):
            if self.mat2[i][0] == ".":
                counter_x += 1
            if self.mat2[0][i] == ".":
                counter_y += 1
        if counter_x == counter_y:
            return "collapse"
        return "made it"

    def starting(self):
        for i in range(0, row):
            for j in range(0, col):
                self.mat1.append(".")
            self.mat2.append(self.mat1)
            
    def playable(self, x, y, c):
        for i in range(len(self.mat2)):
            self.mat2[i][x] = c
            self.mat2[y][i] = c

    def display(self):
        for i in range(len(self.mat2)):
            for j in range(len(self.mat2[i])):
                print(self.mat2[i][j])
            print("") 
        

row = int(input("row: "))
col = int(input("col: "))

game_counter = int(input("game count: "))

start = 1
end = game_counter

gameObject = GamePad(row, col)

while start <= end:
    target_x = int(input("Targeting for x: "))
    target_y = int(input("Targetting for y: "))
    character = str(input("character: ")) 

    targeting = Target(target_x, target_y, character)
    gameObject.playable(targeting.get_x(), targeting.get_y(), targeting.fill_target())

    
    gameObject.display()
    
    start += 1



print(gameObject.coordination_check()) 



