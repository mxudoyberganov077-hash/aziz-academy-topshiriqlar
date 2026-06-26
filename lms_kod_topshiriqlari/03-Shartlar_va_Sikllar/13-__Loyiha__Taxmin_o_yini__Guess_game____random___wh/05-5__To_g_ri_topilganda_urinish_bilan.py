secret = 4
count = 0
while True:
    guess = int(input())
    count += 1
    if guess == secret:
        print(f"Correct in {count} tries")
        break