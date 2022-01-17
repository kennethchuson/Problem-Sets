



size = int(input())


arr = []

result = 0

start = 0
while start < size:
    numbers = int(input("number: ")) 
    arr.append(numbers) 
    start += 1


check_if_not_sort = False

for i in range(len(arr)):
    if arr[i] > arr[len(arr) - 1]:
        check_if_not_sort = True


if check_if_not_sort:
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                t = arr[i]
                arr[i] = arr[j]
                arr[j] = t


dict_result = {}
for i in range(len(arr)):
    if arr[i] in dict_result:
        dict_result[arr[i]] += 1
    else:
        dict_result[arr[i]] = 1 

print(dict_result) 
    
