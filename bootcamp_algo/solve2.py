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


'''
Given in an alumni interview in 2021.
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 
  
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
'''


def solve_problem2(str1):
    index = 0
    ans = "" 
    size = len(str1)
    if size <= 2:
        return str1
    while index != size:
        count = 1
        while (index < size - 1) and (str1[index] == str1[index + 1]):
            count += 1
            index += 1
        if count == 1:
            ans += str(str1[index]) 
        elif count > 1:
            ans += str(str1[index]) + str(count)
        index += 1

    return ans 
                                    
        

str1 = "aaaabbcddd";
expected1 = "a4b2c1d3";

out2 = solve_problem2(str1)

print("problem 2: ", out2)


'''
  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
'''


def solve_problem3(str1):
    return str1 == str1[::-1] 
    


str2 = "racecar";
expected2 = True;
  
str3 = "Dud";
expected3 = False;
  
str4 = "oho!";
expected4 = False;

out3 = solve_problem3(str2)

print("problem 3: ", out3) 
















