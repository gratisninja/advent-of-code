param_count = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3}
with open("input_5.txt") as f:
    arr = [int(a) for a in f.readline().split(',')]
i = 0
while i < len(arr):
    dont_move = False
    mode_list = []
    param_list = []
    if arr[i] == 99:
        break
    if arr[i] > 99:
        mode_list = [int(a) for a in reversed(str(arr[i])[:-2])]
        arr[i] = int(str(arr[i])[-2:])
    for c in range(1, param_count[arr[i]] + 1):
        param_list.append(arr[i+c] if len(mode_list) >= c and mode_list[c-1] == 1 else arr[arr[i+c]])
    if arr[i] == 1:
        arr[arr[i+3]] = param_list[0] + param_list[1]
    elif arr[i] == 2:
        arr[arr[i+3]] = param_list[0] * param_list[1]
    elif arr[i] == 3:
        inp = input('User input: ')
        arr[arr[i+1]] = int(inp)
    elif arr[i] == 4:
        print(param_list[0])
    elif arr[i] == 5:
        if param_list[0] != 0:
            i = param_list[1]
            dont_move = True
    elif arr[i] == 6:
        if param_list[0] == 0:
            i = param_list[1]
            dont_move = True
    elif arr[i] == 7:
        arr[arr[i+3]] = 1 if param_list[0] < param_list[1] else 0
    elif arr[i] == 8:
        arr[arr[i+3]] = 1 if param_list[0] == param_list[1] else 0
    if arr[i] in param_count:
        if not dont_move:
            i += param_count[arr[i]] + 1
