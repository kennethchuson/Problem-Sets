

#distinct powers

'''
2^2=4, 2^3=8, 2^4=16, 2^5=32
3^2=9, 3^3=27, 3^4=81, 3^5=243
4^2=16, 4^3=64, 4^4=256, 4^5=1024
5^2=25, 5^3=125, 5^4=625, 5^5=3125
'''

def solve1(start, end):
    store = []
    for i in range(start, end):
        for j in range(start, end):
            store.append(pow(i, j))
    return store


n_start = 2
n_end = 5

out = solve1(n_start, n_end)

print("Distinc power: ", out) 


