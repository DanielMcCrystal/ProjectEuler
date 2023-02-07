import time

def d(stop):
	start = time.time()
	i = 0
	x = 1
	n = 0
	dn = 10 ** n
	prod = 1
	while True:
		for c in str(x):
			i += 1
			if i == dn:
				prod *= int(c)
				dn *= 10
				n += 1
				if n == stop:
					end = time.time()
					print("Time elapsed: " + str(end - start) + "s")
					return prod
		x += 1





print(d(7))