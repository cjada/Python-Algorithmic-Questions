"""
Return the primes contained in a range defined by n. 
"""

def find_primes(n):
	primes = [True for i in range(n + 1)]
	p = 2
	primes[0] = primes[1] = False
	while (p * p) <= n:
		if primes[p]:

			for i in range(p * 2, n + 1, p):
				primes[i] = False

		p += 1

	for p in range(2, n+1):
		if primes[p]:
			print(p)


print(find_primes(25))