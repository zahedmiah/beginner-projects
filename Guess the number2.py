#Guess the number second attempt
#learnt a few important concepts, such as the import module
import random

number = random.randrange(1,50)
guess = int(input(f"guess the number between 1 & 50: "))
while guess != number:
    if guess > number:
        print("Wrong. Try lower next time!")
        guess = int(input(f"guess the number between 1 & 50: "))
    elif guess < number:
        print("Wrong. Try higher next time!")
        guess = int(input(f"guess the number between 1 & 50: "))
    
    
print("Congratulations, you have guessed correctly!")