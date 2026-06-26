secret = 8
count = 0
while True:
    guess = int(input())
    count += 1
    if guess == secret:
        print("Correct")
        break
    elif count == 1:
        print("Low" if guess < secret else "High")
    else:
        print("Wrong")
    