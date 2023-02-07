
import sympy

def ans(max):
	primes = [x for x in sympy.sieve.primerange(2, max)]
	print("done generating primes")

	best_start = 0
	best_end = 0
	best_sum = primes[0]

	start = best_start
	end = best_end
	sum = best_sum
	while True:
		#print(str(end-start))
		original_sum = sum
		if original_sum >= max:
			return (primes[best_start], primes[best_end], (best_end - best_start + 1), best_sum)
		for new_end in range(end+1, len(primes)):
			sum += primes[new_end]
			if sum >= max:
				break
			if sympy.isprime(sum) and (new_end - start > best_end - best_start):
				best_start = start
				best_end = new_end
				best_sum = sum
				original_sum = sum
		sum = original_sum
		sum -= primes[start]
		start += 1
		end = start + (best_end - best_start)
		sum += primes[end]

	print(best_sum)
	print(primes[best_start:best_end+1])
	return (primes[best_start], primes[best_end], (best_end - best_start + 1), best_sum)

print(ans(1000000))