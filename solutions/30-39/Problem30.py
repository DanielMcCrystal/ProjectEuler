
def sum_of_all(n):
    matches = []
    x = 2;
    s = sum_of_pow(x, n)
    while x < 10000000:
        if x==s:
            print(x)
            matches.append(x)
        x+=1
        s = sum_of_pow(x, n)

    sum = 0
    for i in matches:
        sum += i
    return sum

def sum_of_pow(m, n):
    sum = 0
    while m > 0:
        sum += (m%10)**n
        m /= 10
        m = int(m)
    return sum

print(sum_of_all(5))
print("done")