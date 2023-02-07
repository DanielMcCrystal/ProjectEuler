
def is_palindrome(str_n):
	a = 0
	b = len(str_n) - 1
	while a < b:
		if not str_n[a] == str_n[b]:
			return False
		a += 1
		b -= 1
	return True

def base_2(n):
	str_2 = ''
	x = n
	while x > 0:
		str_2 = str(x % 2) + str_2
		x //= 2
	return str_2

sum = 0
for i in range(1000000):
	if is_palindrome(str(i)) and is_palindrome(base_2(i)):
		sum += i

print(sum)