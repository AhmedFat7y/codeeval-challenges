import sys


def extract_digits(line):
  result = ''
  base = ord('a')
  possible_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
  for c in line:
    if c.isdigit():
      result += c
    elif c in possible_chars:
      result += str(ord(c) - base)
  print(result if result else 'NONE')


with open(sys.argv[1], 'r') as test_cases:
  for test in test_cases:
    if not test:
      continue
    extract_digits(test.rstrip())
