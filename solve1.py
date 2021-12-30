


#Project Euler


"""

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

def multiples(n):
    result_sum = 0
    if n >= 1000:
        return n
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            result_sum += i
    return result_sum

n = 10
out_1 = multiples(n)

print("Multipels of 3 or 5: ", out_1)


"""

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

"""


def evenFib(n):
    a = 1
    b = 1
    result = 0
    while a <= n:
        if a % 2 == 0:
            result += a
        a = b
        b = a + b
    return result

for i in range(0, n):
    out_2 = evenFib(i) 
    print("Even Fibonacci numbers: ", out_2)


"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def Largest_Prime_Factor(n):

    i = 3
    factor = []
    while pow(n, 2) <= n:
        if n % i != 0:
            i += 2
        else:
            n /= i
            factor.append(i)
            
    while n >= i:
        if n % i != 0:
            i += 2
        else:
            n /= i
            factor.append(i)
            
    return max(factor) 
    
        

n2 = 600851475143

out_3 = Largest_Prime_Factor(n2)

print("Largest prime factor: ", out_3)























