storage = {
        "A": [4,3,5,8],
        "B": [2,1,8,9],
        "C": [1,1,9,4]
    }

target_a = 5
target_b = 9
target_c = 8

for (k, v) in storage.items():
    v.sort()

right_a = 0
right_b = 0
right_c = 0
left_a = len(storage.values()[0]) - 1 
left_b = len(storage.values()[1]) - 1 
left_c = len(storage.values()[2]) - 1

idx_a = 0
idx_b = 0
idx_c = 0

while right_a < left_a:
    mid1 = (left_a + right_a) / 2
    if storage.values()[0][mid1] == target_a:
        key = ""
        for (k, v) in storage.items():
            if storage.values()[0][mid1] in v:
             key = k 
        idx_a = (key, mid1) 
    if storage.values()[0][mid1] < target_a: 
        right_a = mid1 + 1
    else:
        left_a = mid1 - 1
        
while right_b < left_b:
    mid2 = (left_b + right_b) / 2
    if storage.values()[1][mid2] == target_b:
        key = ""
        for (k, v) in storage.items():
            if storage.values()[1][mid2] in v:
             key = k 
        idx_b = (key, mid2) 
    if storage.values()[1][mid2] < target_b: 
        right_b = mid2 + 1
    else:
        left_b = mid2 - 1
        
while right_c < left_c:
    mid3 = (left_c + right_c) / 2
    if storage.values()[2][mid3] == target_c:
        key = ""
        for (k, v) in storage.items():
            if storage.values()[2][mid3] in v:
             key = k 
        idx_c = (key, mid3) 
    if storage.values()[2][mid3] < target_c: 
        right_c = mid3 + 1
    else:
        left_c = mid3 - 1

print(idx_a)
print(idx_b)
print(idx_c)
