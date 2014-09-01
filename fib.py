# Generate the Fibonacci sequence up to term N

from sys import argv

def fib(m, n = None, cache = None):

  if n is None:
    i = 2
  else:
    i = n
  if cache is None:
    cache = (0, 1)
    if i > 0:
      i -= 2
  while i > 0:
    cache = (cache[1], sum(cache))
    i -= 1
  while m >= 0:
    n_1 = sum(cache)
    print n, n_1, cache
    if i == 0:
      print
      i += 1
    cache = (cache[1], n_1)
    m -= 1
    n += 1


def main():
  if len(argv) == 2:
    fib(int(argv[1]))
  elif len(argv) == 3:
    fib(int(argv[1]), int(argv[2]))
  else:
    print """Usage: python fib.py <M> [<N>]
    Where <M> is the number of terms to show in the fibonacci sequence
    Where <N> is the first term to start showing from"""
    return

if __name__ == "__main__":
  main()
