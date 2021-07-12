class Selected:
    def __init__(self, selected_number):
        self.number = int(selected_number)

    def __lt__(self, other):
        return self.number < int(other)

    def __eq__(self, other):
        return self.number == int(other)

    def __gt__(self, other):
        return self.number > int(other)


if __name__ == '__main__':
    import random
    selected = Selected(random.randint(1, 100))
    print("I'm thinking of a number between 1 and 100")
    guesses = set([])
    while True:
        guess = input("    Guess a number ")
        guesses.add(guess)
        if guess < selected:
            print(" - your guess is too small")
        elif guess > selected:
            print(" - your guess is too large")
        else:
            print(" - your guess is CORRECT")
            break
    print(f'You guessed {len(guesses)} times')

