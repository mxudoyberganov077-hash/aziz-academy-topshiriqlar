secret = 15
while True:
    guess = int(input())
    if guess == secret:
        print("Correct")
        break
    elif abs(guess - secret) >= 5:
        print("Far")
    else:
        print("Close")