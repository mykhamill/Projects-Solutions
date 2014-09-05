#!/usr/bin/python
# -*- coding: latin-1 -*-

# **Binary to Decimal and Back Converter**
# - Develop a converter to convert a decimal number to binary or a binary number
# to its decimal equivalent.

import argparse
from sys import argv
from math import ceil

def convert(dec=None, bi=None):
  if bi is not None:
    return " ".join((lambda x: [(x[i * 8: (i + 1) * 8]) for i in range(len(x) / 8)])
                    (("{0:0" + str(int(ceil(len(bin(bi)[2:]) / 8.0) * 8)) + "b}").format(bi)))
  if dec is not None:
    return str(int('0b' + dec, 2))

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-b', '--to-binary', type=int,
                      help="the decimal number that will be converted to binary")
  parser.add_argument('-d', '--to-decimal', type=str,
                      help="the binary number that will be converted to decimal")

  if len(argv) == 1:
    parser.print_help()
    return
  args = vars(parser.parse_args())
  if args["to_decimal"] is not None:
    print convert(dec=args["to_decimal"])
  if args["to_binary"] is not None:
    print convert(bi=args["to_binary"])

if __name__ == '__main__':
  main()
