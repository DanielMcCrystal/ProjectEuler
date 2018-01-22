from sympy import sieve


def is_pandigital(number, n):
	n_str = str(number)
	if len(n_str) != n:
		return False
	seen = [False] * n
	for c in n_str:
		digit = int(c)
		if digit == 0 or digit > n or seen[digit - 1]:
			return False
		else:
			seen[digit - 1] = True
	return True

primes = [x for x in sieve.primerange(1, 7654321)]
print("Done generating primes")
for i in range(len(primes)-1, 0, -1):
	if is_pandigital(primes[i], 4) or is_pandigital(primes[i], 7):
		print(primes[i])
		break

print("done")