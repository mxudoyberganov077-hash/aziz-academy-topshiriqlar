secret = 9
while True:
    a = int(input())
    if a < secret:
        print("Low")
    elif a > secret:
        print("High")
    else:
        print("Correct")
        break
       