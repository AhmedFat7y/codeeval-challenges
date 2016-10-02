result = ''
for i in range(1, 13, 1):
  row = ''
  for j in range(1, 13, 1):
    row += str(i * j).rjust(4)
  result += row.strip() + '\n'
print(result.strip())
