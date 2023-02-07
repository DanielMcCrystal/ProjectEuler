
import bisect
import math

primes = [2]

def is_prime(n):
    sqrt = math.sqrt(n)
    for prime in primes:
        if prime > sqrt:
            return True
        if n % prime == 0:
            return False
    return True

def generate_primes():
    for x in range(3, 10000):
        if is_prime(x):
            primes.append(x)

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found

def is_prime_clean(n):
    return binarySearch(primes, n)

def numPrimes(a, b):
    ans = 0
    n = 0
    while(True):
        ans = (n**2) + (a*n) + b
        # print(str(n) + "^2 + " + str(a) + "(" + str(n) + ") + " + str(b) + " = " + str(ans))
        if is_prime_clean(ans):
           n+=1
        else:
            break
    return n

generate_primes()
print("Done with primes")
'''
max = -1
maxA = 0
maxB = 0
for a in range(-999, 1000):
    for b in range(-999, 1000):
        x = numPrimes(a, b)
        if x > max:
            max = x
            maxA = a
            maxB = b
print("A: " + str(maxA))
print("B: " + str(maxB))
print("Max: " + str(max))
print("Product: " + str(maxA*maxB))
'''