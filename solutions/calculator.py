#!/usr/bin/python
# -*- coding: latin-1 -*-

# **Calculator**
# A simple calculator to do basic operators. Make it a scientific calculator
# for added complexity.

# repl-calc
# take input
# parse input
# compute result
# output result

# valid operations:-
# stage 1: +, -, *, /
# stage 2: (, ), m, m+, m-,
# stage 3: sqrt, ^, log, ln, !, e, pi
# stage 4: rad, deg, sin, cos, tan

# valid input:-
# stage 1: integers
# stage 2: floats
# stage 3: exp notation?
# stage 4: other bases?

# Stage 1 calculator
import logging
import readline
import os

LOG_FILENAME = "/tmp/cal.log"
HISTORY_FILENAME = "/tmp/cal.hist"

logging.basicConfig(filename = LOG_FILENAME,
                    level=logging.DEBUG,)

def get_history_item():
  return [readline.get_history_item(i) for i in xrange(1, readline.get_current_history_length() + 1)]

add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y

class Main(object):
  def __init__(self):
    self.cont = True
    self.operators = ['/', '*', '+', '-'] # operations in bodmas order
    self.op_func = [div, mul, add, sub]
    self.parsetree_root = []
    self.prompt = " >: "
    self.input = ""
    self.output = ""
    self.matches = []
    # if os.path.exists(HISTORY_FILENAME):
    #   readline.read_history_file(HISTORY_FILENAME)
    # readline.set_completer(Main.complete)
    # readline.set_completion_display_matches_hook(Main.history_display)
    # readline.parse_and_bind("tab: complete")

  def complete(self, text, state):
    response = None
    if state == 0:
      history_values = get_history_items()
      logging.debug("history: {}".format(history_values))
      if text:
        self.matches = sorted(h for h in history_values if h and h.startswith(text))
      else:
        self.matches = []
      logging.debug("matches: {}".format(self.matches))
    try:
      response = self.prompt + " " + self.matches[state]
    except IndexError:
      response = None
    logging.debug("complete({}{}) => {}".format(repr(text), state, repr(response)))
    return response

  def history_display(self, sub, matches, longest_match_length):
    logging.debug("history_dispy: sub = %s, matches = %s, lml = %s" % (sub, repr(matches, longest_match_length)))

  def display_prompt(self):
    print "\n" + self.prompt,

  def read_input(self):
    self.input = raw_input().strip()

  def parse_calculation(self):
    input = self.input
    if input.lower() in ["quit", "q", "exit"]:
      self.cont = False
      return
    output = "**" + input + "** being parsed\n Please wait...."
    self.output = output

  def display_output(self):
    print '\n' + self.output

  def main(self):
    try:
      while self.cont:
        self.display_prompt()
        self.read_input()
        self.parse_calculation()
        if self.cont:
          self.display_output()
    finally:
      # readline.write_history_file(HISTORY_FILENAME)

run = Main()
main = run.main
if __name__ == '__main__':
  main()
