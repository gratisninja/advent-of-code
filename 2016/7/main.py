#part 1
tls_counter = 0
ips = [line.strip() for line in open("7_input.txt", "r")]
for i in ips:
    supports = False
    abba_allowed = True
    bracket_open = 0
    a = 3
    while a < len(i):
        if i[a] == '[':
            bracket_open += 1
        if i[a] == ']':
            bracket_open -= 1
        if i[a-3] == i[a] and i[a-2] == i[a-1] and i[a-3] != i[a-2] and i[a-1] != i[a]:
            if bracket_open == 0:
                supports = True
            else:
                supports = False
                break
        a = a + 1
    tls_counter += 1 if supports else 0

print('Part 1: ' + str(tls_counter))

#part 2
ssl_counter = 0
for i in ips:
    supports = False
    brackets = [num for num, a in enumerate(i) if a == '['] + [num for num, a in enumerate(i) if a == ']']
    brackets.sort()
    a = 2
    while a < len(i):
        if i[a-2] == i[a] and i[a-1] != i[a]:
            search_for = i[a-1] + i[a] + i[a-1]
            for o in range(0,len(brackets), 2):
                if i[brackets[o]+1:brackets[o+1]].find(search_for) != -1:
                    supports = True
                    a = len(i)
                    break
        a += 1
        if a in brackets:
            a = brackets[brackets.index(a)+1] + 3
    ssl_counter += 1 if supports else 0
print('Part 2: ' + str(ssl_counter))
