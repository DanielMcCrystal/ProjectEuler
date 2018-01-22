
class Solver:
	def __init__(self):
		self.sum = 0

	def has_unique_digits(self, n, length):
		digits = [False]*9
		tmp = n
		for i in range(length):
			digit = int(tmp % 10)
			if digits[digit-1] or digit==0:
				return False
			digits[digit-1] = True
			tmp /= 10
		return True


	def factors(self, n):
		for x in range(12, 99):
			for y in range(123, 988):
				if x * y == n:
					composite = x*10000000 + y*10000 + n
					if(self.has_unique_digits(composite, 9)):
						print(str(x) + " * " + str(y) + " = " + str(n))
						self.sum += n
						return
		for x in range(2, 10):
			for y in range(1234, 9877):
				if x * y == n:
					composite = x * 100000000 + y * 10000 + n
					if (self.has_unique_digits(composite, 9)):
						print(str(x) + " * " + str(y) + " = " + str(n))
						self.sum += n
						return

solve = Solver()
for n in range(1234, 9877):
	if solve.has_unique_digits(n, 4):
		solve.factors(n)

print("Sum = " + str(solve.sum))
