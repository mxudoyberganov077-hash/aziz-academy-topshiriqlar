secret = 1
attempts = 0
while True:
    guess = int(input())
    attempts += 1
    if guess == secret:
        print("Correct")
        break
    else:
        print("Try again")
print(attempts)