import random

def guess_the_number():
    # Step 2: Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100.")
    print("Can you guess what it is?")

    # Step 3: Use a loop to repeatedly ask for the user's guess
    while True:
        # Step 4: Get the user's guess and increment the attempt count
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Step 5: Check if the guess is too high, too low, or correct
        if guess < number_to_guess:
            print("Your guess is too low. Try again!")
        elif guess > number_to_guess:
            print("Your guess is too high. Try again!")
        else:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break

# Run the game
guess_the_number()
