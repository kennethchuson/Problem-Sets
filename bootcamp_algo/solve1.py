'''
Acronyms
Create a function that, given a String, returns the string's Acronyms
(first letter of each word capitalized).
Do it with split first if you need toString, then try to do it without


'''



def solve_problem1(str1):

    splitting = str1.split()
    size = len(splitting)
    store = []
    ans = "" 
    for i in range(size):
        store.append(splitting[i][0])

    for i in range(len(store)):
        ans += store[i].capitalize()

    return ans
    


str1 = " there's no free lunch - gotta pay yer way. ";
expected1 = "TNFL-GPYW";

str2 = "Live from New York, it's Saturday Night!";
expected2 = "LFNYISN";


out1 = solve_problem1(str1)

print("solve problem 1: ", out1)

'''
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
'''

def solve_problem2(str1):
   
    size = len(str1) - 1
    ans = "" 
    while size >= 0:
        ans += str1[size] 
        size -= 1
    return ans


str3 = "creature";
expected = "erutaerc";

str4 = "dog";
expected3 = "god";

out2 = solve_problem2(str3)

print("solve problem 2: ", out2)








