# Give the next prime number until asked to stop

from sys import argv

is_prime = lambda y, p: ((map(lambda x: y % x, p)).count(0) == 0)

def next_prime(n, p = None):
    if p is None:
      p = [2]
    i = n + 1
    while not is_prime(i, p):
      i += 1
    return i, p + [i]

def primes(y = None):
  if y is None:
    cont = ["y"]
  else:
    cont = ["y"] * y
  i, n, p = 1, 2, None
  text = "prime {i} is, {n}"
  while len(cont) > 0 and cont[0] == "y":
    print text.format(i = i, n = n)
    n, p= next_prime(n, p)
    i += 1
    cont = cont[1:]
    if len(cont) == 0:
      cont = raw_input("Would you like to continue the sequence? [Y/N] ").lower().strip()
      if cont.isdigit():
        cont = ["y"] * int(cont)
  print "--Sequence Ended at prime {i}--".format(i = i - 1)
  return

def main():
  if len(argv) == 1:
    primes()
  elif len(argv) == 2:
    primes(int(argv[1]))
  else:
    print """Usage: python next_prime.py [<N>]
    Each prime will be output, the user will then get a choice to continue or stop
    Where <N> is an optional parameter to output before giving the choice to continue"""
    return

if __name__ == '__main__':
  main()
