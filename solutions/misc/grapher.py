import math

def pow(x):
	return x**x


def print_graph(function, width, height):
	data = [None]*width
	for i in range(width):
		data[i] = function(i)
	magnitude = max(data)
	for h in range(height, 0, -1):

		print("|", end="")
		for w in range(width):
			if data[w] >= (magnitude / height) * h and data[w] < (magnitude / height) * (h + 1): 
				print(" *", end="")
			else:
				print("  ", end="")
		print("")
	print("|", end="")
	for w in range(width):
		print("__", end="")
	print("")

def f(x):
	try:
		return 0.3 * math.sin(x)
	except ValueError:
		return 0


print_graph(f, 80, 40)

