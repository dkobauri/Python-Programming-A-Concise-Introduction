import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    reals = []
    while len(reals) != 10:
        reals.append(random.random() * 5 + 30)
    print(reals)

problem2_4()