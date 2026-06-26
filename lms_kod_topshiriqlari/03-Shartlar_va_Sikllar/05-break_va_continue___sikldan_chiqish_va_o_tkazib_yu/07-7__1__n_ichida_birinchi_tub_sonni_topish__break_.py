n = int(input())
if n < 2:
    print("No")
else:
    for i in range(2, n + 1 ):
        tub = True
        for j in range(2, i):
            if i % j == 0:
                tub = False
                break
        if tub:
            print(i)
            break