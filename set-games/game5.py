
show_arr = ['O', 'X', 'Y', 'O', 'P']
show_arr2 = ['O', 'X', 'Y', 'O', 'P']


hide_arr = []
hide_arr2 = [] 

for i in range(len(show_arr)):
    hide_arr.append("*")

for i in range(len(show_arr2)):
    hide_arr2.append("*") 




start_game = True
compare_a = ''
compare_b = ''
while start_game:
    guess_one = int(input())


    for i in range(len(hide_arr)):
        hide_arr[guess_one] = show_arr[guess_one]
        if hide_arr[guess_one] != "*": 
            compare_a = hide_arr[guess_one] 
        print(hide_arr[i]) 
        
    guess_two = int(input())
    
    for i in range(len(hide_arr2)):
        hide_arr2[guess_two] = show_arr2[guess_two]
        if hide_arr2[guess_two] != "*": 
            compare_b = hide_arr2[guess_two] 
        print(hide_arr[i])

    print("A: ", compare_a)
    print("B: ", compare_b) 
    if compare_a == compare_b:
        break
    else:
        continue


print("won!") 
