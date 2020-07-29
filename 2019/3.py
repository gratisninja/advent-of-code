import time

curr_time = time.time()

inp_arr = []
for f in open("input_3.txt"):
    inp_arr.append(f.split(','))
wire1 = [0,0]
wire1_list = []
for a in inp_arr[0]:
    direc = a[0]
    no = int(a[1:])
    for i in range(no):
        if direc == "U":
            wire1[0] += 1
        elif direc == "R":
            wire1[1] += 1
        elif direc == "D":
            wire1[0] -= 1
        else:
            wire1[1] -= 1
        wire1_list.append((wire1[0], wire1[1]))

wire2 = [0,0]
wire2_list = []
for a in inp_arr[1]:
    direc = a[0]
    no = int(a[1:])
    for i in range(no):
        if direc == "U":
            wire2[0] += 1
        elif direc == "R":
            wire2[1] += 1
        elif direc == "D":
            wire2[0] -= 1
        else:
            wire2[1] -= 1
        wire2_list.append((wire2[0], wire2[1]))

inters = list(set(wire1_list).intersection(set(wire2_list)))
inters_dist_to_zero = [abs(i[0]) + abs(i[1]) for i in inters]
inters_dist_to_zero.sort()
print('Part 1: {}'.format(inters_dist_to_zero[0]))
print('Start time: {} Curr time: {} Duration: {}'.format(curr_time, time.time(), time.time()-curr_time))
curr_time = time.time()

inters_dist_to_last = []
for inter in inters:
    inters_dist_to_last.append(wire1_list.index(inter) + 1 + wire2_list.index(inter) + 1) # +1 because (0,0) is missing

print('Part 2: {}'.format(min(inters_dist_to_last)))
print('Start time: {} Curr time: {} Duration: {}'.format(curr_time, time.time(), time.time()-curr_time))
