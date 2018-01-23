import sympy
import math

def answer(n):
	p = 7
	while True:
		p = sympy.nextprime(p)
		print(p)
		for repeated_set in repeated_digits(p):
			count = 0
			first = -1
			for k in range(10):
				check = replace_digits(p, repeated_set, k)
				if check != -1 and sympy.isprime(check):
					if first == -1:
						first = check
					count += 1
					if count == n:
						return first


def repeated_digits(p):
	digits = str(p)
	indices = [[] for x in range(10)]

	for i in range(len(digits)):
		d = digits[i]
		indices[int(d)].append(i)

	return [x for x in indices if len(x) > 0 and len(x) < len(digits)]

def replace_digits(n, indices, d):
	list_n = list(str(n))
	for i in indices:
		if i == 0 and d == 0:
			return -1
		list_n[i] = str(d)
	return int("".join(list_n))



print(answer(8))