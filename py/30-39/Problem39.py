
# p = a + b + c
# p - (a + b) = c
# c^2 = a^2 + b^2
# p = a + b + sqrt(a^2 + b^2)
import math
'''
max = 0
max_p = 0
for p in range(0, 1000, 6):
	count = 0
	for a in range(1, p):
		for b in range(a, p):
			c = math.sqrt(a**2 + b**2)
			if c != int(c):
				continue
			c = int(c)

			sum = a + b + c
			if sum > p:
				break
			elif sum == p:
				#print("a: " + str(a) + ", b: " + str(b) + ", c: " + str(c))
				count += 1
	if count > max:
		print(p)
		max = count
		max_p = p

print(max_p)
'''

n = 1000
nsol = [0] * 1001
for a in range(1, n+1):
	for b in range(a, n+1):
		c = math.sqrt(a**2 + b**2)
		if c != int(c):
			continue
		p = a + b + int(c)
		if p >= 1000:
			continue
		nsol[p] += 1

print(nsol.index(max(nsol)))