a = open('input.txt', 'r').read().replace(' ', '')
arr = [0,0,0,0]
way = 0
for i in a.split(','):
  way = way + 1 if i[0] == 'R' else way - 1
  if way == 4 or way == -4:
    way = 0
  arr[way] += int(i[1:])
print(abs(arr[0]-arr[2]) + abs(arr[1] - arr[3]))
