import sys


def fizz_buzz(line):
  X, Y, n = tuple([int(i) for i in line.split(' ')])
  output_seq = ['1']
  for i in range(2, n + 1, 1):
    result_str = ''
    if i / X == i // X:
      result_str = 'F'
    if i / Y == i // Y:
      result_str += 'B'
    if not result_str:
      result_str = str(i)
    output_seq.append(result_str)
  print(' '.join(output_seq))


with open(sys.argv[1], 'r') as test_cases:
  for test in test_cases:
    if not test:
      continue
    fizz_buzz(test.rstrip())
