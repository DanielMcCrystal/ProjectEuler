
def get_all_pandigital_nums():
	for x in pandigital_rec('', '1234567890'):
		yield int(x)

def pandigital_rec(used, unused):
	if len(unused) == 0:
		yield used
	else:
		for i in unused:
			cp_used = str(used)
			cp_used += i
			cp_unused = unused.replace(str(i), '')
			for x in pandigital_rec(cp_used, cp_unused):
				yield x

def digits_divisible_by(n, start, div):
	n_str = str(n)
	sub_int = int(n_str[start-1:start + 2])
	return sub_int % div == 0

def has_property(n):
	starts = range(2, 9)
	divs = [2, 3, 5, 7, 11, 13, 17]
	for i in range(len(starts)):
		if not digits_divisible_by(n, starts[i], divs[i]):
			return False
	return True

def answer():
	sum = 0
	for x in get_all_pandigital_nums():
		if has_property(x):
			sum += x
			print("pan: " + str(x))
			print(sum)
			print()
	return sum

print(answer())