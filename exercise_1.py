import random

def guessing_game():
    number = random.randint(0, 100)
    message = "Guess a number, between 0 and 100:\n"
    guess = -1
    while guess != number:
        guess = input(message)
        if guess == '':
            print("That is not a number, try again")
            continue
        guess = int(guess)
        if guess > number:
            print(f'{guess} is too high')
        elif guess < number:
            print(f'{guess} is too low')
        else:
            print(f'{guess} is just right')


if __name__ == "__main__":
    guessing_game()