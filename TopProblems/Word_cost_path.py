def check_collapse(direction_path):
    check = False
    for (x, y) in direction_path:
        if x == y:
            check = True
            res = (x, y)

    return [check, res] 


def solve(board, word, num):
    rows = len(board)
    cols = len(board[0])
    path = set()
    path_val = []
    total_cost = 0
    direction_path = []
    mes = "possible"
    mes2 = "not collapse" 

    def dfs(r, c, curr):
        tup = (r, c) 
        if curr == len(word):
            return
        if (r < 0 or c < 0 or r >= rows or c >= cols or word[curr] != board[r][c][0] or tup in path):
            return
        path.add(tup)
        direction_path.append(tup) 
        path_val.append(board[r][c][1])
        res = (dfs(r + 1, c, curr + 1) or
               dfs(r - 1, c, curr + 1) or
               dfs(r, c + 1, curr + 1) or
               dfs(r, c - 1, curr + 1))
        path.remove(tup)
        return res


    for i in range(rows):
        for j in range(cols):
            dfs(i, j, 0) 
    
    for i in range(len(path_val)):
        total_cost += path_val[i]
        
    if total_cost > num:
        mes = "not possible"
        
    if check_collapse(direction_path)[0]:
        mes2 = "collapse: " + str(check_collapse(direction_path)[1]) 
        
                
    return (direction_path, total_cost, mes, mes2) 
    




board = [
         [("A", 2), ("B", 5), ("C", 2), ("E", 6)],
         [("S", 1), ("F", 4), ("C", 1), ("S",9)],
         [("A", 3), ("D", 4), ("E", 2), ("E", 10)]
        ]


word = "ABCCED"
num = len(word) 


out = solve(board, word, num)
print(out)
