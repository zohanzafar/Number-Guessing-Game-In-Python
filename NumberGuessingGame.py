import random
import math

print("\"Welcome to Number Guessing Game\"\n")

# Enter the lower and upper bound range
lowerBound = int(input("Enter the lower bound: "))
upperBound = int(input("Enter the upper bound: "))

# A random number is selected from the given range
randomNum = random.randrange(lowerBound, upperBound)

# This formula will generate the number of guesses (chances to guess the number)
noOfGuessing = math.ceil(math.log2(upperBound - lowerBound + 1))

# Save the number of chances left
leftGuesses = noOfGuessing

# Counter for guesses
i = 0

while i < noOfGuessing:
    # User enters the number
    num = int(input("\nEnter the number: "))

    # Print the number of tries left
    print("Guesses Left: ", leftGuesses)
    leftGuesses -= 1
    i += 1

    # Check the number according to the condition
    if num == randomNum:
        print("Congratulations! You have guessed the number")
        break
    elif num > randomNum:
        print("You guessed too high")
    elif num < randomNum:
        print("You guessed too small")

# When the user wins, exit the loop without printing "Game Over"
if num == randomNum:
    pass
else:
    print("\n\"Game Over\"")
    print("The number is ", randomNum)
    print("Better Luck Next time!")