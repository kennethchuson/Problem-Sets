res = []


def solve(i, j, n, s, count):
    if n == i or n == j:
        res.append((s, count))
        return
    solve(i + 1, j + 1, n, s + ")", count + 1)
    
    for k in range(i + 1):
        solve(i + 1, j + k, n, s + "<", count - 1)
        
    solve(i + 1, j + 1,  n, s + "(", count + 1)
    
    for k in range(i + 1):
        solve(i + 1, j + k, n, s + ">", count - 1) 
    
        
        
n = int(input())
s = ""
count = 0

measures = []
i_j_directions = []

for i in range(n + 1):
    if i <= 0:
        continue
    for j in range(n + 1): 
        solve(i, j, n, s, count)


for (x, y) in res:
    measures.append(x)
    i_j_directions.append(y)

print(measures)
print(i_j_directions)
