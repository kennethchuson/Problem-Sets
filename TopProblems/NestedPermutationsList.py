def solve(nums, start, end, res, child_res):
    
    if start == end:
        res.append(nums.copy())
        child_res.append(nums.copy()) 
        return
    for i in range(start, end + 1):
        temp = nums[start]
        nums[start] = nums[i]
        nums[i] = temp
 
        for j in range(len(nums[i][2])):
            temp2 = nums[start][2][j]
            nums[start][2][i] = nums[i][2][j]
            nums[i][2][j] = temp2

            solve(nums, start + 1, end, res, child_res)

            temp2 = nums[start][2][j]
            nums[start][2][i] = nums[i][2][j]
            nums[i][2][j] = temp2
            
        temp = nums[start]
        nums[start] = nums[i]
        nums[i] = temp

        

nums = [('A', 1, [11, 12, 13]),('B', 2, [21, 22, 23]),('C', 3, [31, 32, 33])]

start = 0
end = len(nums) - 1

res = []
child_res = [] 

out = solve(nums, start, end, res, child_res)

print(res)
print(child_res)
