inp = [line.strip() for line in open("1_input.txt", "r")]
for a in inp:
    print(str(a.count('(') - a.count(')')))
    pos = 1
    for i,o in enumerate(a):
        pos += 1 if o == '(' else -1
        if pos == -1:
            print(i)
            break
