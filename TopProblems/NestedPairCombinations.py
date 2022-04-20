def solve(n, k):
    res = []
    def dfs(start, comb):
        if len(comb) == k:
            res.append(comb.copy())
            return
        for i in range(start, n + 1):
            for j in range(start, n + 1):
                pair = (i, j)
                comb.append(pair)
                dfs(i + 1, comb)
                comb.pop() 
    dfs(1, [])

    return res 


n = 4
k = 2


out = solve(n, k)
print(out) 
