
def tri_n(n):
	return 0.5 * n * (n + 1)

def convert_word(s):
	sum = 0
	for c in s:
		sum += ord(c) - 64
	return sum


tris = set()
for n in range(100):
	tris.add(tri_n(n))

words_file = open('p042_words.txt', 'r')
tmp = words_file.read()
words = tmp.split(sep="\",\"")
words[0] = words[0][1:]
words[-1] = words[-1][:-1]

count = 0
for word in words:
	if convert_word(word) in tris:
		count += 1
print(count)