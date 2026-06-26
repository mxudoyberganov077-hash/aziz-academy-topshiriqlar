
a = set(map(int, input().split()))
b = set(map(int, input().split()))
res = b - a
if res:
    print(*sorted(res))
else:
    print("BO'SH")
