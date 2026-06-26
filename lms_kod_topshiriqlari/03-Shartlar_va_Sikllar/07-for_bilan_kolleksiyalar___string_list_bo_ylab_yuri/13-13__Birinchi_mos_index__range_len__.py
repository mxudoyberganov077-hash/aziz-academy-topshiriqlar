n = int(input())
numbers = list(map(int, input().split()))
qidirilayotgan = int(input())
index = -1
for i in range(len(numbers)):
    if numbers[i] == qidirilayotgan:
        index = i
        break
print(index)