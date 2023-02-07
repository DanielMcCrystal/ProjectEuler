
import sympy
import math

# both methods assume n is prime
def trunc_left(n):
	x = int(str(n)[1:])
	while x > 0:
		if not sympy.isprime(x):
			return False
		if len(str(x)) > 1:
			x = int(str(x)[1:])
		else:
			x = -1
	return True

def trunc_right(n):
	x = n // 10
	while x > 0:
		if not sympy.isprime(x):
			return False
		x //= 10
	return True


counter = 0
i = 10
sum = 0
while counter < 11:
	if sympy.isprime(i):
		if trunc_left(i) and trunc_right(i):
			sum += i
			counter += 1
			print("value: " + str(i))
			print("counter: " + str(counter))
			print()
	i += 1

print("sum: " + str(sum))