
import sympy

def is_circular(n):
	digits = [c for c in str(n)]
	if not sympy.isprime(n):
		return False
	for i in range(1, len(digits)):
		tmp = digits[-i:] + digits[:len(digits)-i]
		if not sympy.isprime(int(''.join(tmp))):
			return False

	return True


count = 0
for i in range(1000000):
	if is_circular(i):
		count += 1
print(count)