# Finding Pi to the Nth digit

import sys
from math import factorial, ceil

def double_factorial(n):
  return reduce(lambda x, y: x * y, [x for x in range(int(n + 1)) if x % 2 == n % 2 and x > 0], 1)

def pi_to_Nth(n):
  return 2 * sum([factorial(x)/(double_factorial((2 * x) + 1) * 1.0) for x in range(int(n + 1))])

def main():
  if len(sys.argv) > 1:
    n = int(sys.argv[1])
  else:
    print """Usage: Pi_to_Nth <N>\nWhere <N> is the number of digits to show Pi to"""
    return
  print ("{pi:." + str(n + 1) + "}").format(pi = pi_to_Nth(ceil(n // 3) * 10))

if __name__ == "__main__":
  main()
