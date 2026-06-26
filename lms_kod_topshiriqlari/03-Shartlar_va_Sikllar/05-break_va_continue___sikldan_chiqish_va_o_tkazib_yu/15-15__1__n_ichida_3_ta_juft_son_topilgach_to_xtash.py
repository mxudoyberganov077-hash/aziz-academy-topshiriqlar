n = int(input())
i = 0
count = 0
while i < n:
    i += 1
    if i % 2 == 0:
        count += 1
        if count == 3:
            print(i)
            break
else:
    print("No")
