import sys


def find_highest(line):
  rows = [row.strip() for row in line.split('|')]
  max_cols = []
  length = 0
  for row in rows:
    cols = [int(x) for x in row.split(' ')]
    if not max_cols:
      max_cols = cols
      length = len(cols)
    else:
      max_cols = [cols[i] if cols[i] > max_cols[i] else max_cols[i] for i in range(length)]
  print(' '.join([str(max_col) for max_col in max_cols]))


with open(sys.argv[1], 'r') as test_cases:
  for test in test_cases:
    if not test:
      continue
    find_highest(test)
