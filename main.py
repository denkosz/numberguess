import random
def guess(a):

    print(f"You have {a} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if a == 1:
        return print(f"You've run out of guesses, you lose.\nThe correct answer is {computer_num}")
    if user_guess == computer_num:
        print(f"You got it! The answer was {computer_num}")
    if user_guess > computer_num:
        print("To high.")
        a = a - 1
        print("Guess again")
        guess(a)
    if user_guess < computer_num:
        print("Too Low.")
        a = a - 1
        print("Guess again")
        guess(a)

def difficulty():
    total_c = 5
    total_b = 10
    if user_diff == "hard":
        guess(total_c)
    elif user_diff == "easy":
        guess(total_b)


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
computer_num = random.randint(1, 100)
user_diff = input("Choose difficulty. Type 'easy' and 'hard': ")
difficulty()
