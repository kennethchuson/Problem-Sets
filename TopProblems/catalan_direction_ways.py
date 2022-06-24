store = []


def solve(n, s):
    res = 0
    
    if n <= 1:
        return 1
    
    store.append((n, s)) 
    
    for i in range(n):
        res += solve(i, s + '<') * solve(n - i - 1, s + '>') 
    return res


n = int(input()) 


i = 0
s = ""
 
while i < n + 1:
    out = solve(i, s)
    print(str(i) + " : " + str(out)) 
    i += 1


print(store) 
