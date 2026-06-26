secret = 10
attempts = 0
while attempts < 5:
    guess = int(input())
    attempts += 1
    if guess == secret:
        print("Correct")
        break
else:
    print("You lost")
       
    