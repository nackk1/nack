import random

HEADS = 1
TAILS = 2
TOSSES = 10

def tosses_coin():
    for i in range(TOSSES):
        if random.randint(HEADS, TAILS) == HEADS:
            print("HEADS")
        else:
            print("TAILS")

tosses_coin()