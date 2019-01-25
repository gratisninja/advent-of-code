messages = [line.strip() for line in open("6_input.txt", "r")]
pos = [{} for a in messages[0]]
for message in messages:
    for i, a in enumerate(message):
        if a in pos[i]:
            pos[i][a] += 1
        else:
            pos[i][a] = 1
print('Part 1: ' + ''.join([max(a, key=a.get) for a in pos]))
print('Part 2: ' + ''.join([min(a, key=a.get) for a in pos]))
