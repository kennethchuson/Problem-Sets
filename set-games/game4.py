



class World(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_all_coordinates(self):
        for i in range(self.x):
            for j in range(self.y):
                for k in range(self.z):
                    print("x: ", i)
                    print("y: " ,j)
                    print("z: ", k)
    





class Person(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mat = []
        self.mat2 = [] 
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def print_coordinates(self, x_given = 0, y_given = 0):
        for i in range(x_given):
            for j in range(y_give):
                mat.append(x_given)
            mat2.append(mat)
        return [mat,  mat2]
    
    def fucking_swapper():
        pass



def solve1(a, b):

    a = 1
    if a <= b:
        for i in range(a, (a + b)):
            for j in range(i + 1, (a + b) / 2):
                a = pow(i, j)
    return a

def solve2(a, b, c):
    store = []
    personalize = Person(a, b)
    for i in range(personalize.get_x()):
        for j in range(personalize.get_y()):
            s = set()
            s.add({i, j})
    return [s] 



store = [] 
while True:
    n = int(input()) 
    for i in range(0, 10):
        store.append(n)
    start = 0
    end = len(store) - 1
    while start <= end:
        for i in range(end, -1, -1):
            reversing = solve1(store[i], store[i - 1])
        if reversing == -1:
            print("error try again") 
            continue
        else:
            break
        start += 1
        
