import random

specialNumber = random.randint(1,5)
attempts = 3

print("Guess a number between 1 and 5:")

for x in range(attempts):
    userInput = int(input())
    
    if (userInput == specialNumber):
        print("That's the number!")
        break
    else:
        print("That's not the number. Try again.")

if userInput != specialNumber:
    print(f"Sorry, you've used up your {attempts} attemtps. The correct answer was {specialNumber}.")