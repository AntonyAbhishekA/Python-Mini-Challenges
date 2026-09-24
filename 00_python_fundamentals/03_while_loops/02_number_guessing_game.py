guess = 0
ans = 4

while guess != ans:
    guess = int(input("Enter your guess: "))

    if guess < ans:
        print("Too low!")

    elif guess > ans:
        print("Too high!")

    else:
        print("Congratulations! You've guessed the correct number.")