def tri(n):
	return int(n * (n+1) / 2)

def pent(n):
	return int(n * (3 * n - 1) / 2)

def hex(n):
	return int(n * (2 * n - 1))

tri_n = 1
pent_n = 1
hex_n = 1

tri_val = tri(1)
pent_val = pent(1)
hex_val = hex(1)

while True:
	if tri_val < pent_val:
		tri_n += 1
		tri_val = tri(tri_n)
	elif pent_val < hex_val:
		pent_n += 1
		pent_val = pent(pent_n)
	elif tri_val == pent_val == hex_val:
		print("Match at " + str(tri_val))
		print("T(" + str(tri_n) + ")")
		print("P(" + str(pent_n) + ")")
		print("H(" + str(hex_n) + ")")
		print()
		if tri_val > 40755:
			break
		tri_n += 1
		pent_n += 1
		hex_n += 1
		tri_val = tri(tri_n)
		pent_val = pent(pent_n)
		hex_val = hex(hex_n)

	else:
		hex_n += 1
		hex_val = hex(hex_n)