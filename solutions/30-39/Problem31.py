
coins = [1, 2, 5, 10, 20, 50, 100, 200]

def unique_ways(p):
    if p == 0:
        return 1

    lower_den = unique_ways(p-1)
    amount = int(lower_den*(lower_den+1)/2)

    if not coins[p]%coins[p-1] == 0:
        amount *= unique_ways(p-2)

    return amount+1


print(unique_ways(3))

