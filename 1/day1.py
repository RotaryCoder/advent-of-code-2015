
f = open('input.txt', 'r')
data = f.read()

j = 0
position = 0

for i in data:
  position += 1
  if i == '(':
    j += 1
  elif i == ')':
    j -= 1
  else:
    print(i)

  if j == -1:
    break

print()
print('j= %s' % j)
print('position= %s' % position)
