import math

factorials = [math.factorial(x) for x in range(10)]

def fact_sum(n):
	x = n
	sum = 0
	while x > 0:
		sum += factorials[x%10]
		if sum > n:
			return -1
		x //= 10
	return sum

sum = 0
#print(factorials)

i = 10
while i <= 100000000:
	if fact_sum(i) == i:
		print(i)

		sum += i
		print("new sum: " + str(sum))
		num_digits = int(math.log10(i))
		for n in range(num_digits):
			i += int(math.pow(10, n))
	else:
		i+=1

print("sum: " + str(sum))
