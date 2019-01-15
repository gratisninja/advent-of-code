# part 1
keypad = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9']]

pos = [1, 1]
code = ''

instr = open("D:/Ausbildungsinhalte/Python/AoC/2016/2_input.txt", "r")
for line in instr.readlines():
    for i in line:
        if i == 'U':
            pos[1] = pos[1] - 1 if pos[1] > 0 else pos[1]
        if i == 'D':
            pos[1] = pos[1] + 1 if pos[1] < 2 else pos[1]
        if i == 'L':
            pos[0] = pos[0] - 1 if pos[0] > 0 else pos[0]
        if i == 'R':
            pos[0] = pos[0] + 1 if pos[0] < 2 else pos[0]
    code += keypad[pos[1]][pos[0]]

print(code)
instr.close()

# part 2
keypad = [['X', 'X', '1', 'X', 'X'],
          ['X', '2', '3', '4', 'X'],
          ['5', '6', '7', '8', '9'],
          ['X', 'A', 'B', 'C', 'X'],
          ['X', 'X', 'D', 'X', 'X']]

pos = [0, 2]
code = ''

instr = open("D:/Ausbildungsinhalte/Python/AoC/2016/2_input.txt", "r")
for line in instr.readlines():
    for i in line:
        prev_pos = pos.copy()
        if i == 'U':
            pos[1] = pos[1] - 1 if pos[1] > 0 else pos[1]
        if i == 'D':
            pos[1] = pos[1] + 1 if pos[1] < 4 else pos[1]
        if i == 'L':
            pos[0] = pos[0] - 1 if pos[0] > 0 else pos[0]
        if i == 'R':
            pos[0] = pos[0] + 1 if pos[0] < 4 else pos[0]
        if keypad[pos[1]][pos[0]] == 'X':
            pos = prev_pos.copy()
    code += keypad[pos[1]][pos[0]]

print(code)
instr.close()
