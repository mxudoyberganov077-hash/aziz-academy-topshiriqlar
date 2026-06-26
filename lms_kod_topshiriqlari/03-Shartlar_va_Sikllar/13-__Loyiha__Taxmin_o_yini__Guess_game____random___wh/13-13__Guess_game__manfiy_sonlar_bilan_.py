secret = -4
count = 0
while True:
    guess = int(input())
    count += 1
    if guess > secret:
        print("High")
    elif guess < secret:
        print("Low")
    else:
        print("Correct")
        break