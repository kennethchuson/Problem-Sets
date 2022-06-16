n = int(input())


coin = 5



how_many = 0
coins_need = [] 

if coin > n:
    print("error!")
else:
    i = 1
    while i < n:
        calc = coin * i
        if calc <= n:
            how_many = i 
            coins_need.append(calc) 
        i += 1


print(how_many) 
print(coins_need)
