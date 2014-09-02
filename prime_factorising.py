# Get the prime factors of <N>

from sys import argv
from math import sqrt

is_prime = lambda y, p: ((map(lambda x: y % x, p)).count(0) == 0)

def next_prime(n, p = None):
    if p is None:
        p = [2]
    i = n + 1
    while not is_prime(i, p):
        i += 1
    return i, p + [i]

def get_primes(n):
    j, p = next_prime(2)
    if n < 3:
        return p
    else:
        while j < n:
            j, p = next_prime(j, p)
        return p

def get_factors(n):
  sqrt_n = sqrt(n)
  primes = get_primes(sqrt_n)
  primes = [y for (x, y) in [(n % x, x) for x in primes] if x == 0]
  m = n
  prime_factors = []
  for p in primes:
    i, j = m / p, m % p
    while j == 0:
      prime_factors.append(p)
      m = i
      i, j = m / p, m % p
  if m != 1:
    m, n = primes.append(m), prime_factors.append(m)
  prime_factors = dict(zip(primes, [prime_factors.count(p) for p in primes]))
  print ", ".join(["{k}^{v}".format(k = k, v = v) for k,v in prime_factors.items()])

def main():
  if len(argv) == 2:
    get_factors(int(argv[1]))
  else:
    print """Usage: python prime_factorising.py <N>
    Where <N> is the number to be factorised"""
    return

if __name__ == '__main__':
  main()
