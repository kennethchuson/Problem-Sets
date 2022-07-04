import random



inputting = input() + 1


arr = [i for i in range(inputting)] 


n = len(arr)

splitting = 2

res = []
guesses = set() 

while n != 0:
    for i in range(1, len(arr), n):
        a = arr[i: i + n]
        if len(a) <= 1:
            continue
        print(a)
        choosing_r = random.choice(a)
        guesses.add(choosing_r) 
        print("guess: " + str(choosing_r)) 
        res.append(a) 
    n /= 2


print("Possible guesses: " + str(list(guesses)))
