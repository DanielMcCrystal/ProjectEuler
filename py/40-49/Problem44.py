
def pent(n):
	return int(n * (3*n - 1) / 2)

pents_set = set()
for i in range(10000):
	pents_set.add(pent(i+1))

pents_list = [pent(i+1) for i in range(10000)]
print("lists created, beginning search...")
k = 1
while k < 10000:
	#print("trying k = " + str(k))
	j = k-1
	while j >= 0:
		Pk = pents_list[k]
		Pj = pents_list[j]
		if Pk - Pj in pents_set and Pk + Pj in pents_set:
			print("Pk = " + str(Pk))
			print("Pj = " + str(Pj))
			print(str(Pk - Pj))
			break
		j -= 1
	else:
		k += 1
		continue
	break