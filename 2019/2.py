with open("input_2.txt") as f:
    inp = f.readline()
inp = [int(a) for a in inp.split(',')]
arr = inp.copy()
arr[1] = 12
arr[2] = 2
for i in range(0, len(arr), 4):
    if arr[i] == 99:
        break
    elif arr[i] == 1:
        arr[arr[i+3]] = arr[arr[i+1]] + arr[arr[i+2]] 
    elif arr[i] == 2:
        arr[arr[i+3]] = arr[arr[i+1]] * arr[arr[i+2]]
print("Part 1: {}".format(arr[0]))

for noun in range(100):
    for verb in range(100):
        arr = inp.copy()
        arr[1] = noun
        arr[2] = verb
        for i in range(0, len(arr), 4):
            if arr[i] == 99:
                break
            elif arr[i] == 1:
                arr[arr[i+3]] = arr[arr[i+1]] + arr[arr[i+2]] 
            elif arr[i] == 2:
                arr[arr[i+3]] = arr[arr[i+1]] * arr[arr[i+2]]
        if arr[0] == 19690720:
            print("Part 2: {}".format(100 * noun + verb))
            break
