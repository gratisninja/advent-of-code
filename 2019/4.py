import time
start = time.time()

count = 0
for i in [str(i) for i in range(367479, 893699)]:
    eligible = True
    has_repeating = False
    for ind in range(1,6):
        if int(i[ind]) < int(i[ind-1]):
            eligible = False
            break
        elif int(i[ind]) == int(i[ind-1]):
            has_repeating = True
    if not has_repeating:
        eligible = False
    if eligible:
        count += 1
print('Part 1: {}'.format(count))
print('Start time: {} Curr time: {} Duration: {}'.format(start, time.time(), time.time()-start))
start = time.time()

count = 0
for i in [str(i) for i in range(367479, 893699)]:
    eligible = True
    has_repeating = False
    for ind in range(1,6):
        if int(i[ind]) < int(i[ind-1]):
            eligible = False
            break
        elif int(i[ind]) == int(i[ind-1]) and not has_repeating:
            has_repeating = not (ind - 2 >= 0 and int(i[ind-2]) == int(i[ind]) or ind + 1 <= 5 and int(i[ind+1]) == int(i[ind]))
    if not has_repeating:
        eligible = False
    if eligible:
        count += 1
print('Part 2: {}'.format(count))

print('Start time: {} Curr time: {} Duration: {}'.format(start, time.time(), time.time()-start))