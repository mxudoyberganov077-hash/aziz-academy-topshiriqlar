s = 42

while True:
    n = int(input())
    if n < s:
        print("Low")
    elif n > s:
        print("High")
    else:
        print("Correct")
        break

 