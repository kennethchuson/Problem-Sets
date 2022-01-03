'''

Given an arr and a separator string, output a string of every item in the array separated by the separator.
  
No trailing separator at the end
Default the separator to a comma with a space after it if no separator is provided

'''

def solve_problem1(arr, sep):
    size = len(arr)
    new_arr = ""
    for i in range(size):
        new_arr += str(arr[i]) 
        if i < size - 1:
            new_arr += sep
    return new_arr
        

arr1 = [1, 2, 3];
separator1 = ", ";
expected1 = "1, 2, 3";

arr2 = [1, 2, 3];
separator2 = "-";
expected2 = "1-2-3";

arr3 = [1, 2, 3];
separator3 = " - ";
expected3 = "1 - 2 - 3";

out1 = solve_problem1(arr2, separator2)

print("solve problem 1: ", out1)




