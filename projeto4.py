import random
import os

number = random.randint(1, 10)
guess = input("Adivinhe um numero de 1 até 10" )
guess = int(guess)

if guess == number:
    print("Você acertou!")
else:
    print("Você errou tente novamente!")