import sys


def reconstruct_sentence(line):
  data = line.split(';')
  sentence = data[0]
  indecies = data[1]
  words = zip (sentence.split(' '), indecies.split(' '))
  words.so


with open(sys.argv[1], 'r') as test_cases:
  for test in test_cases:
    if not test:
      continue
    reconstruct_sentence(test)
