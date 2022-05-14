'''


arr = [1, 2, 2, 3, 3, 5, 9, 21]

arr2 = [(1, 2), (2, 3), (3, 5), (5, 9), (9, 21)]

next:
    [(1,2), (2,3)] = 2 * 2 + 1 * 3 = 7 
    .
    .
    .
    [(5,9), (9,21)] = 9 * 9 + 21 * 5 = 186

                                    sum = 264




'''

arr = [3,21,2,2,5,3,1,9]

arr.sort()

res = []
for i in range(len(arr) - 1):
    if (arr[i] == arr[i + 1]):
        continue 
    tup = (arr[i], arr[i + 1])
    res.append(tup)

res2 = []

for i in range(len(res) - 1):
    res2.append([res[i], res[i + 1]])

ans = 0
for i in range(len(res2)):
    ans += (res2[i][0][1] * res2[i][1][0] + res2[i][0][0] * res2[i][1][1])
print(ans)
