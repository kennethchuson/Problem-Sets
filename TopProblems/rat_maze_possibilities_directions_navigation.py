N = 4


sol = [ [ 0 for j in range(N) ] for i in range(N) ]



def isSafe(maze, x, y):
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True
    return False

def possibilities(n, left, right, s, ans):
    if left == n and right == n:
        ans.append(s)
        return
    
    if left < n:
        possibilities(n, left + 1, right, s + '(<-)', ans) 

    if right < left:
        possibilities(n, left, right + 1, s + '(->)', ans)


def solveMaze(maze):
    

    if solveMazeUtil(maze, 0, 0, sol) == False:
        print("Solution doesn't exist")
        return False

    return True


def solveMazeUtil(maze, x, y, sol):

    if x == N - 1 and y == N - 1:
        sol[x][y] = 1
        return True

    if isSafe(maze, x, y):
        
        sol[x][y] = 1

        if solveMazeUtil(maze, x + 1, y, sol):
            return True

        if solveMazeUtil(maze, x, y + 1, sol):
            return True

        sol[x][y] = 0
        return False

def finalSolve():
    c = "" 


    count_c1 = 0
    count_c2 = 0
    count_c3 = 0
    count_c4 = 0
    count_r1 = 0
    count_r2 = 0
    count_r3 = 0
    count_r4 = 0 

    for i in range(len(sol)):
        c = sol[0][i]
        r = sol[i][0] 
        if c == 1:
            count_c1 += 1
        if r == 1:
            count_r1 += 1
            
    for i in range(len(sol)):
        c = sol[1][i]
        r = sol[i][1] 
        if c == 1:
            count_c2 += 1
        if r == 1:
            count_r2 += 1
            
    for i in range(len(sol)):
        c = sol[2][i]
        r = sol[i][2] 
        if c == 1:
            count_c3 += 1
        if r == 1:
            count_r3 += 1 
            
    for i in range(len(sol)):
        c = sol[3][i]
        r = sol[i][3] 
        if c == 1:
            count_c4 += 1
        if r == 1:
            count_r4 += 1

    output_c = [count_c1, count_c2, count_c3, count_c4]
    output_r = [count_r1, count_r2, count_r3, count_r4]

    ans_c = []
    dic_c = {} 
    for i in range(len(output_c)):
        possibilities(output_c[i], 0, 0, "", ans_c)
        

    ans_r = []
    for i in range(len(output_r)):
        possibilities(output_r[i], 0, 0, "", ans_r) 


    print("col") 
    print(ans_c)

    print("row") 
    print(ans_r)



if __name__ == "__main__": 

    maze = [ [1, 0, 0, 0], 
             [1, 1, 0, 1], 
             [0, 1, 0, 0], 
             [1, 1, 1, 1] ]
    '''
    maze = [ [1, 0, 0, 1, 1, 0, 0, 1],
             [1, 1, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 1, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 0, 1, 0],
             [0, 1, 0, 1, 0, 0, 1, 0],
             [0, 1, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 1, 1, 1, 1] ]
    '''
               
    solveMaze(maze)

    finalSolve() 
