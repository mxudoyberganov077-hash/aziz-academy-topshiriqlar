a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = set(map(int, input().split()))

common = a & b & c

print(*sorted(common))