
import random 





store = []

got = 0 

attempts = 0

n = int(input("Up to what number?: ")) 


while True:
    m = int(input("Guess a number: "))
    
    if m <= 0:
        print("should be positive number, try again")
        continue
    
    for i in range(1, m):
        store.append(i)
        
    if random.choice(store) == m:
        got = m
        break
    else:
        attempts += 1
        continue

print("you finally got ", m, " with ", attempts, " attempts!") 
        




arr = [32,3,3,4,4,4,5]

print(random.choice(arr)) 
