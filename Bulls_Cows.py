"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Iveta Minaříková
email: pilatovaiveta@gmail.com
discord: ivet_13 (Iveta M.)
"""
import random
import time

print("Hi there!")
print("-----------------------------------------------")
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print("Enter a 4-digit number with unique digits, not starting with zero.")
print("Bull means you guessed the correct number and position. Cow means correct number but wrong position.")
print("Have fun!")
print("-----------------------------------------------")


def generate_secret_number():
    digits = random.sample(range(1, 10), 4)
    return ''.join(map(str, digits))

# Function checks, if guess is valid and can be used for evaluation (4-digit number with unique digits, not starting with zero).
def guess_check(guess):
    if not guess.isdigit() or len(set(guess)) != 4 or guess[0] == '0':
        return False
    else:
        return True

# Function evaluates a players guess and returns number of bulls and cows. 
def guess_evaluation(secret_number, guess):
    bulls = 0
    for i in range(len(secret_number)):
        if secret_number[i] == guess[i]:
            bulls += 1
    
    cows = 0
    for g in guess:
        if g in secret_number:
            cows += 1
    cows -= bulls
    return bulls, cows

# Prints singular or plural form of the word (cow, bull) based on counts.
def print_result(bulls, cows):
    bull_word = "bull" if bulls == 1 else "bulls"
    cow_word = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bull_word}, {cows} {cow_word}")

# Evaluating score based on number of attempts.
def score(attempts):
    if attempts <= 5:
        return "amazing"
    elif attempts <= 10:
        return "average"
    else:
        return "not so good"

def main():
    secret_number = generate_secret_number()
    attempts = 0
    start_time = time.time()
    
    while True:
        guess = input("Enter a number:\n-----------------------------------------------\n>>> ")
        
        if not guess_check(guess):
            print("Invalid input. Please enter a 4-digit number with unique digits, not starting with zero.")
            continue
        
        attempts += 1
        bulls, cows = guess_evaluation(secret_number, guess)
        
        if bulls == 4:
            elapsed_time = time.time() - start_time
            performance = score(attempts)
            print(f"Correct, you've guessed the right number in {attempts} guesses!")
            print(f"Elapsed time: {elapsed_time:.2f} seconds")
            print(f"That's {performance}.")
            break
        
        print_result(bulls, cows)

if __name__ == "__main__":
    main()
