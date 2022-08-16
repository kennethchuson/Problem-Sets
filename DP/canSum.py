'''

arr = [5,3,4,7]

        3 + 4 = 7 
        
traget = 7

    output: True


'''

#recursion
def solve(target, nums):
    if target == 0:
        return True

    if target < 0:
        return False
    
    for i in range(len(nums)):
        rem = target - nums[i]
        if solve(rem, nums):
            return True
    return False


print("recursion: ") 
print(solve(7, [2,3]))
print(solve(7, [5,3,4,7]))
print(solve(7, [2,3]))
print(solve(7, [2,4]))


def solve2(target, nums, memo={}):

    if target in memo:
        return memo[target] 
    
    if target == 0:
        return True

    if target < 0:
        return False
    
    for i in range(len(nums)):
        rem = target - nums[i]
        if solve(rem, nums):
            memo[target] = True 
            return True
    memo[target] = False
    return False


print("recursion: ") 
print(solve2(7, [2,3]))
print(solve2(7, [5,3,4,7]))
print(solve2(7, [2,3]))
print(solve2(7, [2,4]))
