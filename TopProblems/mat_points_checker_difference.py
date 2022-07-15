mat = [
        ['.', '.', 'X'],
        ['X', '.', '.'], 
        ['.', 'X', '.'], 
        ['Y', '.', 'Y']
      ]
        


points = 10


r = len(mat)
c = len(mat[0])


diff = 1
res = [] 

for i in range(r):
    sub = [] 
    for j in range(c):
        if(
            (mat[r - 1][j] == 'X' or mat[i][c - 1] == 'X') and
            (mat[r - 1][j] == 'Y' or mat[i][c - 1] == 'Y')
           ):
            points -= 1
        elif mat[r - 1][j] == 'X' or mat[i][c - 1] == 'X':
            points += 1

        for j in range(points):
            diff = (i * j) - points
            sub.append(diff)
    res.append(sub) 
    
            
            

            
print(res) 
        
