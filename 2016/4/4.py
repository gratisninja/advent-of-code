rooms = open("4_input.txt", "r")

def is_number(i):
    try:
        int(i)
        return True
    except ValueError:
        return False

sum_rooms = 0
not_decoy = []
for room in rooms.readlines():
    stop_counting = False
    letters = {}
    number = ''
    for i, a in enumerate(room):
        if is_number(a):
            number = room[i:i+3]
            break
        if a != '-':
            if a in letters:
                letters[a] += 1
            else:
                letters[a] = 1
                
    sorted_letters = [v[0] for v in sorted(letters.items(), key=lambda kv: (-kv[1], kv[0]))]
    for num, i in enumerate(room[room.find('[')+1:]):
        if i == ']':
            not_decoy.append((room[:room.find(number)-1], number))
            sum_rooms += int(number)
            break
        if (not i in sorted_letters) or (sorted_letters[num] != i):
            break


for num, i in enumerate(not_decoy):
    encoded = ''
    for a in i[0]:
        if a == '-':
            encoded += ' '
        else:
            encoded += chr(ord(a) + int(i[1]) % 26) if ord(a) + int(i[1]) % 26 < 123 else chr(97 + int(i[1]) % 26 - (123 - ord(a)))
    not_decoy[num] = (encoded, i[1])

print(not_decoy)
print(sum_rooms)


    


        
    
