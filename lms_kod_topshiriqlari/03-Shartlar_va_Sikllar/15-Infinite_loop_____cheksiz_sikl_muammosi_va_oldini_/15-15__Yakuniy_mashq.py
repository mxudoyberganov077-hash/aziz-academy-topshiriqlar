n = input()
if n == "hello":
    print("Working")
else:
    sonlar = list(map(int, input().split()))
    print(sonlar[0])
    print(sonlar[1:-1])
    print(sonlar[-1])

    