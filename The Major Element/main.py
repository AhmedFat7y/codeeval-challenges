import sys
import collections


def find_major_element(line):
  result = []
  seq = line.split(',')
  min_occurrences = len(seq) // 2
  repetition_counter = collections.Counter(seq)
  for n in repetition_counter:
    if repetition_counter[n] > min_occurrences:
      result.append(n)
  if not result:
    print(None)
  else:
    print(' '.join(result))


with open(sys.argv[1], 'r') as test_cases:
  for test in test_cases:
    if not test:
      continue
    find_major_element(test.rstrip())
