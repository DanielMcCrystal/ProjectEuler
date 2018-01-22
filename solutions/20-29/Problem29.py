import math

import Problem27


def num_single_primes(n):
    sqrt = math.sqrt(n)
    for x in Problem27.primes:
        if x > sqrt:
            return 1, n
        elif n % x == 0:
            test = 1+num_specific_prime(n/x, x)

            if test != -1:
                print(str(n) + ", " + str(test))
                return test, x
            else:
                return -1, n

def num_specific_prime(n, m):
    if n==1:
        return 0
    if n % m == 0:
        test = num_specific_prime(n/m, m)
        if test != -2:
            return 1+test
        else:
            return -2
    else:
        return -2

def num_terms(max_a, max_b):
    max = (max_a - 1)*(max_b - 1)
    for a in range(3, max_a+1):

        value = num_single_primes(a)
        num = int(value[0])
        prime = int(value[1])
        for b in range(2, max_b+1):
            if b*num > max_b:
                break
            elif num > 1:
                print(str(a) + "^(" + str(b) +") = " + str(a**b))
                max-=1
    return max

print(num_terms(100, 100))
