
def solve(arr):
    n = len(arr)
    res = []
    path_pair = [] 

    def dfs(l):
        if l == n - 1:
            res.append(list(arr))
            return
        for i in range(l, n):
            arr[l], arr[i] = arr[i], arr[l]
            path_pair.append((arr[l], arr[i]))
            dfs(l + 1)
            arr[l], arr[i] = arr[i], arr[l]
    dfs(0)
    return [res, path_pair] 


arr = [1,2,3]

out = solve(arr)[0] 

out2 = solve(arr)[1] 

row = len(out)
col = len(out[0])

category = {} 

for (x, y) in out2:
    perm_store = [] 
    for i in range(row): 
        perm_store.append(out[i])
    category[(x, y)] = perm_store

print("Group permutation") 
print(category)
