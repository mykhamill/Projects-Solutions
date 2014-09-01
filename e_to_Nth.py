# Finding e to the Nth digit

from sys import argv
from math import factorial

def e_to_Nth(n):
  return sum([1/(factorial(x) * 1.0) for x in range(n+1)])

def tries(n, last = None):
  if last is None:
    curr = ("{e:." + str(n) + "}").format(e = e_to_Nth(n))
    last = {"x": n, "tri": ""}
  else:
    curr = ("{e:." + str(n) + "}").format(e = e_to_Nth(last['x'] + 1))
  print "Log: curr = ", curr
  print "Log: last = ", last
  if curr == last['tri']:
    return curr
  else:
    last['tri'] = curr
    return tries(n, last)

def main():
  if len(argv) > 1:
    n = int(argv[1])
  else:
    print "Usage: python e_to_Nth.py <N>\nWhere <N> is the number of digits to show e to"
    return
  print ("{e:." + str(n) + "}").format(e = e_to_Nth(n))
  print tries(n)

if __name__ == "__main__":
  main()
