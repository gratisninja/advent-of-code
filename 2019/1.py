
import math
fuel = 0
input_arr = []
for f in open("input_1.txt"):
    input_arr.append(int(f))
    fuel += math.floor(input_arr[-1] / 3) - 2
print("Part 1: {}".format(fuel))

fuel = 0
for f in input_arr:
    while True:
        f = math.floor(f / 3) - 2
        if f <= 0:
            break
        fuel += f
print("Part 2: {}".format(fuel))