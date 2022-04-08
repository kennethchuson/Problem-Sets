def findClosest_number(arr, count):
    curr = arr[0] 
    for val in arr: 
        if abs(count - val) < abs(count - curr): 
            curr = val 
    return curr
    

def solve(passengers, count, A_inter):
    size = len(passengers)
    
    output = 0 
    
    for i in range(size - 1):
        for j in range(i + 1, size):
            if passengers[i] < passengers[j]:
                count += 1
            else:
                count -= 1
                
    get_list_of_routes = [] 
    
    for i in range(len(A_inter)): 
        routes = A_inter[i][1] 
        get_list_of_routes.append(routes) 
    
    closest = findClosest_number(get_list_of_routes, count) 
    
    for i in range(len(A_inter)): 
        if closest == A_inter[i][1]: 
            output = A_inter[i]
        
    return output
    


count = 100
passengers = [5,6,1,2,3]
A_inter = [
            ["Asia", 50],
            ["America", 70],
            ["Africa", 60]
          ]



out = solve(passengers, count, A_inter)

print(out) 
