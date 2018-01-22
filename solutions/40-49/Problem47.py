

def first_n(n):
	prime_factors = [None, None]

	for i in range(2, 2 + n):
		sqrt = int(i ** (1/2))
		tmp = i
		for x in range(2, sqrt+1):
			if tmp % x == 0:
				tmp //= x
				factors = dict(prime_factors[tmp])
				if x in factors:
					factors[x] += 1
				else:
					factors[x] = 1
				prime_factors.append(factors)
				break
		else:
			prime_factors.append({i: 1})

	i = 2 + n
	while True:
		sqrt = int(i ** (1 / 2))
		tmp = i
		for x in range(2, sqrt + 1):
			if tmp % x == 0:
				tmp //= x
				factors = dict(prime_factors[tmp])
				if x in factors:
					factors[x] += 1
				else:
					factors[x] = 1
				prime_factors.append(factors)
				break
		else:
			prime_factors.append({i: 1})

		sets = prime_factors[-n:]
		if len(sets[0]) != n:
			i += 1
			continue
		cumulative_factors = set([(key, sets[0][key]) for key in sets[0]])
		for _set in sets[1:]:
			if len(_set) != n:
				break
			for key in _set:
				if (key, _set[key]) not in cumulative_factors:
					cumulative_factors.add((key, _set[key]))
				else:
					break
			else:
				continue
			break
		else:
			return i - n + 1
		i += 1


print()
print("solution: " + str(first_n(4)))