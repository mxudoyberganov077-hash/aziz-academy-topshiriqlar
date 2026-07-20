start = int(input())
step = int(input())
if start >= 100:
    print(0)
elif step <= 0:
    print("CHEKSIZ")
else:
    qadam = 0
    while start < 100:
        start += step
        qadam += 1
    print(qadam)