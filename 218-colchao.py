d = [int(x) for x in input().split()]
h, l = [int(x) for x in input().split()]

count = 0
for value in d:
    if value <= h:
        count += 1
        d.remove(value)
        break
    else:
        continue

for elemento in d:
    if elemento <= l:
        count += 1
        break
    else: 
        elemento = False

if count >= 2:
    print('S')
else:
    print('N')