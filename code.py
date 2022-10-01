#Setup
from random import*
N=randint(1,30)
i=0
#Code
while i<5:
    P=int(input("Guess a number between 1 and 30: "))
    if N==P:
        print("Good Job!")
        break
    elif N<P:
        i=i+1
        print("Go Less!")
    else:
        i=i+1
        ("Go More!")