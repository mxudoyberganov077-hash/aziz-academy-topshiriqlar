count = 0
total = 0
while True:
    n = int(input())
    if n == 0:
        break
    else:
        total += n
        count += 1
if count == 0:
    print(0)
else:
    print(total / count)