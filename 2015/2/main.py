inp = [line.strip() for line in open("D:/Ausbildungsinhalte/Python/AoC/2015/2_input.txt", "r")]
total = 0
for a in inp:
    l,w,h = list(map(int, a.split('x')))
    total += 2*l*w + 2*w*h + 2*h*l + min(l*w,w*h,h*l)
print(total)

ribbon = 0
for a in inp:
    l = list(map(int, a.split('x')))
    ribbon += sorted(l)[0]*2 + sorted(l)[1]*2 + (l[0]*l[1]*l[2]) 
print(ribbon)
