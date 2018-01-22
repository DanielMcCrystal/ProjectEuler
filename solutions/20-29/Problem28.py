
def sum_of_spiral(n):
    sum = 1
    i = 1
    for x in range(2, n, 2):
        for count in range(0, 4):
            i += x
            sum += i
        x += 2
    return sum

print(sum_of_spiral(1001))
