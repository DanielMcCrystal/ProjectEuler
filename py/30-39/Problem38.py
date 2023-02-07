
def is_pandigital(n):
	n_str = n
	if len(n_str) != 9:
		return False
	seen = [False] * 9
	for c in n_str:
		digit = int(c)
		if seen[digit - 1]:
			return False
		else:
			seen[digit - 1] = True
	return True

def concat(k, n):
	cat = ""
	for i in range(1, n+1):
		cat += str(k * i)
	return cat

max = -1
k = 1
while True:
	for n in range(1, 10):
		cat = concat(k, n)
		if is_pandigital(cat):
			if int(cat) > max:
				max = int(cat)
			print("k = " + str(k))
			print("n = " + str(n))
			print(cat)
			print("Largest: " + str(max))
			print("===============")
			print()
	k += 1