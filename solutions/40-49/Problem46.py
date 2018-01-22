
def valid(n):
	check_prime = 2
	while check_prime <= n - 2:
		check_square = 1
		twice_square = 2
		while twice_square <= n - check_prime:
			twice_square = 2 * (check_square ** 2)
			if twice_square + check_prime == n:
				print(str(n) + " = " + str(check_prime) + " + 2*" + str(check_square) + "^2")
				return True
			check_square += 1
		check_prime = next_prime(check_prime)
	return False

def is_prime(n):
	sqrt = int(n ** (1/2))
	for i in range(2, sqrt + 1):
		if n % i == 0:
			return False
	return True

def next_prime(n):
	n += 1
	while not is_prime(n):
		n += 1
	return n

i = 1
while True:
	if not valid(i) and not is_prime(i):
		break
	i += 2

print("solution: " + str(i))


