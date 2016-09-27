import sys


def extract_words(in_str):
  words = ''
  for c in in_str:
    if c.isalpha():
      words += c.lower()
    elif words and words[-1] != ' ':
      words += ' '
  print (words.rstrip())


with open(sys.argv[1], 'r') as test_cases:
  for test in test_cases:
    if not test: continue
    extract_words(test)

extract_words("(--9Hello----World...--)")
extract_words("Can 0$9 ---you~")
extract_words("13What213are;11you-123+138doing7")
