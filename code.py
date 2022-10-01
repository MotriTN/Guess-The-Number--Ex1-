#Setup
from random import*
N=randint(1,30)
i=0
#Code
while i<5:
    P=int(input("Guess a number between 1 and 30: "))
    if N==P:
        print("You Won!")
        break
    elif N<P:
        i=i+1
        print("Go Less!")
        continue
    else:
        i=i+1
        ("Go More!")
        continue
else:
    print("You Lost :(","The Number was:",N)