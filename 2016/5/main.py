import hashlib
i = 0
pw = ''
while True:
    code = 'cxdnnyjw' + str(i)
    m = hashlib.md5()
    m.update(code.encode('utf-8'))
    hash_code = m.hexdigest()
    if hash_code[:5] == '00000':
        pw += hash_code[5]
        if len(pw) == 8:
            break
    i += 1
print('Teil 1: ' + pw)

i = 0
pw = [' ' for a in range(8)]
while True:
    code = 'cxdnnyjw' + str(i)
    m = hashlib.md5()
    m.update(code.encode('utf-8'))
    hash_code = m.hexdigest()
    if hash_code[:5] == '00000' and hash_code[5].isdigit() and int(hash_code[5]) < 8 and pw[int(hash_code[5])] == ' ':
        pw[int(hash_code[5])] = hash_code[6] 
        if ' ' not in pw:
            break
    i += 1
print('Teil 2: ' + ''.join(pw))
