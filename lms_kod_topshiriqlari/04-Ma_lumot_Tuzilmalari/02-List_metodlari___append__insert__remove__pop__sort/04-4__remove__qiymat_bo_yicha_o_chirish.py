n = int(input())
lst = list(map(int, input().split()))
val = int(input())
if val in lst:
    lst.remove(val)
print(lst)