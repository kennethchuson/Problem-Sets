

'''


[
  ['s', '', ''],
  ['', '', 'E']
]

1.) right, right, down
2.) right, down, right
3) down, right, right


'''

#recursion
def solve(m,n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0 
    return solve(m - 1, n) + solve(m, n - 1) 

print("recursion") 
print(solve(1,1))
print(solve(2,3))
print(solve(3,2))
print(solve(3,3))

#memoization
def solve2(m,n,memo={}):
    key = (m,n)
    
    if key in memo:
        return memo[key]
    
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0 
    memo[key] = solve2(m - 1, n) + solve2(m, n - 1)
    return memo[key] 

print("memoization") 
print(solve2(1,1))
print(solve2(2,3))
print(solve2(3,2))
print(solve2(3,3))


