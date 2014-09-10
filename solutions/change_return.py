#!/usr/bin/python
# -*- coding: latin-1 -*-

# **Change Return Program**
# The user enters a cost and then the amount of money given. The program will
# figure out the change and the number of notes (£5, £10, £20) and
# coins (£1, 50p, 20p, 10p, 5p, 2p, 1p) that are needed for the change.

import argparse
from sys import argv

class Args(object):
  pass

def get_change(c, d):
  ch = {}
  for n in d:
    while c > n:
      c = c - n
      ch[n] = ch.get(n, 0) + 1
  return c, ch

def change(x):
  coins = [100, 50, 20, 10, 5, 2, 1]
  notes = [20, 10, 5]
  i, change_notes = get_change(x, notes)
  i, change_coins = get_change(i * 100, coins)
  return (change_notes, change_coins)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('cost', type=float)
  parser.add_argument('given', type=float)

  args = Args()
  if len(argv) == 1:
    parser.print_help()
    return
  parser.parse_args(namespace=args)
  if args.given < args.cost:
    print "Not enough money given"
    return
  else:
    notes, coins = change(args.given - args.cost)
    for n in reversed(sorted(notes.keys())):
      print "£{n:.2f}:\t{q}".format(n = n, q = notes[n])
    for n in reversed(sorted(coins.keys())):
      print "£{n:.2f}:\t{q}".format(n = (n * 1.0) / 100, q = coins[n])

if __name__ == '__main__':
  main()
