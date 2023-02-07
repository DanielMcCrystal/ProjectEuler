import sympy

def permutations(n1, n2, n3):
	digits = dict()
	for char in str(n1):
		if char not in digits:
			digits[char] = 1
		else:
			digits[char] += 1
	for char in str(n2):
		if char not in digits:
			return False
		else:
			digits[char] += 1
	for char in str(n3):
		if char not in digits:
			return False
		else:
			digits[char] += 1

	for digit in digits:
		if digits[digit] % 3 != 0:
			return False
	return True

def answer():
	start = 1000

	while start < 9997:
		if sympy.isprime(start):
			#print("Checking prime: " + str(start))
			incr = 1
			while start + 2*incr < 10000:
				second = start + incr
				third = start + 2*incr
				if sympy.isprime(second) and sympy.isprime(third) and permutations(start, second, third):
					print("Match! " + str(start) + " " + str(second) + " " + str(third))
					#return
				incr += 1
		start += 1

answer()