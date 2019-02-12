words = [line.strip() for line in open("9_input.txt", "r")]
for a in words:
    res = ""
    i = 0
    while True:
        brace_open_pos = a[i:].find('(') + i
        brace_closed_pos = a[i:].find(')') + i
        if brace_open_pos == -1 + i or i == len(a):
            res += a[i:]
            break
        else:
            res += a[i:brace_open_pos]
            marks = a[brace_open_pos+1:brace_closed_pos].split('x')
            res += a[brace_closed_pos+1:brace_closed_pos+int(marks[0])+1] * int(marks[1])
            i = brace_closed_pos+int(marks[0])+1
    print(res)
    print(len(res))

def process(a):
    if '(' not in a:
        return len(a)
    res = 0
    while a.find('(') > -1:
        res += a.find('(')
        marks = a[a.find('(')+1:a.find(')')].split('x')
        a = a[a.find(')')+1:]
        res += process(a[:int(marks[0])]) * int(marks[1])
        a = a[int(marks[0]):]
    return res

for a in words:
    print(process(a))
