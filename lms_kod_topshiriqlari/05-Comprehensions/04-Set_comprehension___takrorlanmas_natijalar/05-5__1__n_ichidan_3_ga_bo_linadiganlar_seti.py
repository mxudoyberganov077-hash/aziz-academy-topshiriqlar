n = int(input())
s = {i for i in range(1, n + 1) if i % 3 == 0}
if s:
    print(*sorted(s))
else:
    print("BO'SH")