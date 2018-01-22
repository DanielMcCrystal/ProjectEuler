
examples = []
for nu in range(10, 100):
	nu_dig_1 = nu // 10
	nu_dig_2 = nu % 10
	for de in range(nu+1, 100):
		val = nu / de
		de_dig_1 = de // 10
		de_dig_2 = de % 10
		if de_dig_2 == 0:
			continue
		if de_dig_1 == nu_dig_1:
			if nu_dig_2 / de_dig_2 == val:
				examples.append((nu, de))
		elif de_dig_2 == nu_dig_1:
			if nu_dig_2 / de_dig_1 == val:
				examples.append((nu, de))
		elif de_dig_1 == nu_dig_2:		
			if nu_dig_1 / de_dig_2 == val:
				examples.append((nu, de))
		elif de_dig_2 == nu_dig_2:
			if nu_dig_1 / de_dig_1 == val:
				examples.append((nu, de))

num_product = 1
den_product = 1
for x in examples:
	print(str(x[0]) + "/" + str(x[1]))
	num_product *= x[0]
	den_product *= x[1]

divisor = 1
for n in range(2, den_product // 2 + 1):
	if den_product / n == den_product // n and num_product / n == num_product // n:
		divisor = n
print("Divisor: " + str(divisor))
print(str(num_product) + "/" + str(den_product) + " = " + str(num_product // divisor) + "/" + str(den_product // divisor))
