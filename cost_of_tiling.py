# **Find Cost of Tile to Cover W x H Floor**
# Calculate the total cost of tile it would take to cover a floor plan of width
# and height, using a cost entered by the user.

from sys import argv
import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('width', type=int, default=1)
  parser.add_argument('height', type=int, default=1)
  parser.add_argument('--units', type=str, default='metre')
  parser.add_argument('cost', type=float, default=1)
  parser.add_argument('--currency', type=str, default='GBP')

  if len(argv) > 1:
    args = vars(parser.parse_args())
  else:
    parser.print_help()
    return

  for arg, value in args.items():
    if arg == 'width':
      width = value
    elif arg == 'height':
      height = value
    elif arg == 'cost':
      cost = value
    elif arg == 'units':
      units = value
      wunits = value
      hunits = value
    elif arg == 'currency':
      currency = value

  if width > 1:
    wunits = units + "s"
  if height > 1:
    hunits = units + "s"
  if width > 1 or height > 1:
    units = units + "s"

  text = "The cost of tiling the area {w} {wu} by {h} {hu} which is {area} {u} squared is {total_cost:.2f} {c}"
  print text.format(w = width,
                    h = height,
                    area = width * height,
                    total_cost = width * height * cost,
                    wu = wunits,
                    hu = hunits,
                    u = units,
                    c = currency)

  return
if __name__ == '__main__':
  main()
