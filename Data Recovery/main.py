import sys


def reconstruct_sentence(line):
  data = line.split(';')
  words = data[0].split(' ')
  indices = [int(index) for index in data[1].split(' ')]
  words_indices = list(zip(words, indices))
  words_indices.sort(key=lambda t: t[1])
  for i in range(len(words)):
    word_index = words_indices[min(i, len(words_indices) - 1)]
    if word_index[1] != i + 1:
      words_indices.insert(i, (words[-1], i + 1))
      break
  print(' '.join(map(lambda t: t[0], words_indices)))


with open(sys.argv[1], 'r') as test_cases:
  for test in test_cases.readlines():
    if not test:
      continue
    reconstruct_sentence(test.rstrip())
