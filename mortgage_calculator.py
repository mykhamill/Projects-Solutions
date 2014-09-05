#!/usr/bin/python
# -*- coding: latin-1 -*-

# **Mortgage Calculator**
# Calculate the monthly payments of a fixed term mortgage over given Nth terms
# at a given interest rate. Also figure out how long it will take the user to
# pay back the loan. For added complexity, add an option for users to select the
# compounding interval (Monthly, Weekly, Daily, Continually).

import argparse
from sys import argv

class Args(object):
  pass

def cal_payments(c, t, i):
  return c * ((i * (1 + i) ** t) / (((1 + i) ** t) - 1))

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('capital', type=float)
  parser.add_argument('term', type=int, help="is the number of years the mortgage is to be held")
  parser.add_argument('interest', type=float,
                      help="the interest rate to be applied (value is between 0 and 100)")

  args = Args()
  if len(argv) == 1:
    parser.print_help()
    return
  parser.parse_args(namespace=args)
  if 0 > args.interest > 100:
    parser.print_help()
    return
  else:
    text = "{months} installments of £{payments:.2f} to pay off the total amount of £{capital:.2f}"
    payments = cal_payments(args.capital, args.term * 12, args.interest / 100 / 12)
    print (text).format(months = args.term * 12, payments = payments, capital = args.capital)
    return

if __name__ == '__main__':
  main()
