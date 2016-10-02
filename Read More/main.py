import sys


def truncate_sentence(line=''):
  if len(line) <= 55:
    print(line)
  else:
    trimmed_line = line[:line.rfind(' ', 0, 40)]
    print(trimmed_line + '... <Read More>')


with open(sys.argv[1], 'r') as test_cases:
  for test in test_cases:
    if not test:
      continue
    truncate_sentence(test.rstrip())
