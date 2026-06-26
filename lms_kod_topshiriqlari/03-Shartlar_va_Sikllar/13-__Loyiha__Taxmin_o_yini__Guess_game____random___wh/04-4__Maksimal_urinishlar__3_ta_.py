
count = 0
for i in range(3):
    guess = int(input())
    if guess == 8:
        print("Correct")
        break
    else:
        count += 1
        if count == 3:
            print("Game Over")

      
    