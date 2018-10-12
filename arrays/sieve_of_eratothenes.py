"""
Return the primes contained in a range defined by n. 
"""

def find_primes(n):
	primes_list = [i for i in range(2, n + 1)]

	for num in primes_list:
		p = 2
		while (num * p) < (n + 1):
			if (num * p) in primes_list:
				primes_list.remove(num * p)
			p += 1

	return primes_list

