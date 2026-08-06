# Abhishek_jadhav_69137
# Assignment_3

print("NUMBER GUESSING GAME");
print("Guess a number between 1 and 100.");

secret_number = 50;
attempts = 0;

while True:
    guess = int(input("Enter your guess:"));

    if guess < 1 or guess > 100:
        print("Enter a number between 1 and 100.");
        continue;

    attempts += 1;

    if guess > secret_number:
        print("Too High");
    elif guess < secret_number:
        print("Too Low");
    else:
        print("Congratulations You guessed the correct number.");
        print(f"Total attempts used: {attempts}");
        break;