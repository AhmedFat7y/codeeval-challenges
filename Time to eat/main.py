import sys


def sort_timestamps(line):
  timestamps = line.split(' ')
  timestamps[-1] = timestamps[-1].rstrip()
  timestamps.sort()
  timestamps.reverse()
  print(' '.join(timestamps))


with open(sys.argv[1], 'r') as test_cases:
  for test in test_cases:
    if not test:
      continue
    sort_timestamps(test)
