

def last_ten(n):
	sum = 0
	for i in range(1, n+1):
		sum += i**i
	as_str = str(sum)
	print(as_str)
	if len(as_str) > 10:
		return as_str[-10:]
	return as_str

print(last_ten(1000))