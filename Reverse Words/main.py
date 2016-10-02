import sys


def function_call(line):
  sentence = line.split(' ')
  sentence.reverse()
  print(' '.join(sentence))


with open(sys.argv[1], 'r') as test_cases:
  for test in test_cases:
    if not test:
      continue
    function_call(test.rstrip())
