param_count = {1: 3, 2: 3, 3: 1, 4: 1}
with open("input_5.txt") as f:
    arr = f.readline()
arr = [int(a) for a in arr.split(',')]
i = 0
mode_list = []
while i < len(arr):
    if arr[i] == 99:
        break
    if arr[i] > 99:
        mode_list = [int(a) for a in reversed(str(arr[i])[:-2])]
        arr[i] = int(str(arr[i])[-2:])
    if arr[i] < 10:
        param_list = []
        for c in range(1, param_count[arr[i]] + 1):
            param_list.append(arr[i+c] if len(mode_list) >= c and mode_list[c-1] == 1 else arr[arr[i+c]])
    mode_list = []
    if arr[i] == 1:
        arr[arr[i+3]] = param_list[0] + param_list[1]
    elif arr[i] == 2:
        arr[arr[i+3]] = param_list[0] * param_list[1]
    elif arr[i] == 3:
        inp = input('User input: ')
        arr[arr[i+1]] = int(inp)
    elif arr[i] == 4:
        print(param_list[0])
    if arr[i] in param_count:
        i += param_count[arr[i]] + 1