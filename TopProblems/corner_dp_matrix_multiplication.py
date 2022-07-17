mat = [
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.'],
      ]
'''

mat becomes:



 1.)  mat = [
        ['a', '.', '.', 'b'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.'],     
        ['c', '.', '.', 'd'],
      ]

      a = 1
      b = (r - 1) * (c - 1)
      c = (r - 1) * 1
      d = 1 * (c - 1) 

 2.) mat = [
        ['a', 0, 0, 'b'],
        [0, 1, 2, 3],
        [0, 2, 4, 6],     
        ['c', 3, 6, 'd'],
      ]
    
 3.) mat2 = [
              [0, 1, 2, 3],
              [1, 2, 3, 4],
              [2, 3, 4, 5],
              [3, 4, 5, 6]
             ]

  4.) mat1 * mat2
  
        if even: 
            res += dp[i - 1][j][k] + res[i][j - 1][k] + res[i][j][k - 1]
        else:
            res += dp[i - 1][j][k] - res[i][j - 1][k] - res[i][j][k - 1]
            

'''

r = len(mat)
c = len(mat[0])


mult = 1

dp = [[[0 for i in range(r)] for j in range(c)] for k in range(r)] 



mat2 = []
for i in range(r):
    temp = [] 
    for j in range(c):
        temp.append(i + j)
    mat2.append(temp)


for i in range(r):
    for j in range(c):
        if (mat[0][0] == '.' or mat[r - 1][c - 1] == '.' or mat[r - 1][0] == '.' or mat[0][c - 1] == '.'): 
            mat[0][0] = 1
            mat[r - 1][c - 1] = (r - 1) * (c - 1) 
            mat[r - 1][0] = (r - 1) * 1
            mat[0][c - 1] = 1 * (c - 1)

for i in range(r):
    for j in range(c):
        if mat[i][j] == '.':
            mat[i][j] = i * j


for i in range(r):
    for j in range(c):
        for k in range(r):
            mult += mat[i][k] * mat2[k][j]
            if i == 0 and j == 0 and k == 0:
                dp[i][j][k] = 1
            else:
                if mult % 2 == 0: 
                    dp[i][j][k] = (dp[i - 1][j][k] + dp[i][j - 1][k] + dp[i][j][k - 1])
                else:
                    dp[i][j][k] = (dp[i - 1][j][k] - dp[i][j - 1][k] - dp[i][j][k - 1])
        


print(dp)
