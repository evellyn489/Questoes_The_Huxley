n1 = int(input())
n2 = int(input())

count = 0

for i in range(1, 50):
    if (i % n1 == 0) and (i % n2 == 0):
        count += 1

print(count)