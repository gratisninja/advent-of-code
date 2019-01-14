def main():
    a = 'L4, L3, R1, L4, R2, R2, L1, L2, R1, R1, L3, R5, L2, R5, L4, L3, R2, R2, L5, L1, R4, L1, R3, L3, R5, R2, L5, R2, R1, R1, L5, R1, L3, L2, L5, R4, R4, L2, L1, L1, R1, R1, L185, R4, L1, L1, R5, R1, L1, L3, L2, L1, R2, R2, R2, L1, L1, R4, R5, R53, L1, R1, R78, R3, R4, L1, R5, L1, L4, R3, R3, L3, L3, R191, R4, R1, L4, L1, R3, L1, L2, R3, R2, R4, R5, R5, L3, L5, R2, R3, L1, L1, L3, R1, R4, R1, R3, R4, R4, R4, R5, R2, L5, R1, R2, R5, L3, L4, R1, L5, R1, L4, L3, R5, R5, L3, L4, L4, R2, R2, L5, R3, R1, R2, R5, L5, L3, R4, L5, R5, L3, R1, L1, R4, R4, L3, R2, R5, R1, R2, L1, R4, R1, L3, L3, L5, R2, R5, L1, L4, R3, R3, L3, R2, L5, R1, R3, L3, R2, L1, R4, R3, L4, R5, L2, L2, R5, R1, R2, L4, L4, L5, R3, L4'.replace(' ', '')
    #a = open('input.txt', 'r').read().replace(' ', '')
    arr = [0,0,0,0]
    way = 0
    places = [(0,0)]
    x, y = 0, 0
    for i in a.split(','):
        way = way + 1 if i[0] == 'R' else way - 1
        if way == 4 or way == -4:
            way = 0
        for a in range(int(i[1:])):
            arr[way] += 1
            x = x if way in [0, 2, -2] else x + 1 if way in [1, -3] else x - 1
            y = y if way in [-3, -1, 1, 3] else y + 1 if way == 0 else y - 1
            places.append((x, y))
            if places.count(places[-1]) > 1:
                return (abs(arr[0]-arr[2]) + abs(arr[1] - arr[3]))
    return (abs(arr[0]-arr[2]) + abs(arr[1] - arr[3]))

print(main())
