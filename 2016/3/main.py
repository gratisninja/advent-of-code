# part 1
puzinput = open("3_input.txt", "r")
counter = 0
for line in puzinput.readlines():
    sides = [int(a) for a in line.split()]
    if sides[0] + sides[1] > sides[2] and sides[1] + sides[2] > sides[0] and sides[2] + sides[0] > sides[1]:
        counter += 1
print(counter)
puzinput.close()

# part 2

puzinput = open("3_input.txt", "r")
counter = 0
lines = [[int(j) for j in a.split()] for a in puzinput.readlines()]
for i in range(0, len(lines), 3):
    for a in range(3):
        print(lines[i][a], lines[i+1][a], lines[i+2][a])
        if lines[i][a] + lines[i+1][a] > lines[i+2][a] and lines[i+1][a] + lines[i+2][a] > lines[i][a] and lines[i+2][a] + lines[i][a] > lines[i+1][a]:
            counter += 1
print(counter)
print(len(lines))
puzinput.close()
