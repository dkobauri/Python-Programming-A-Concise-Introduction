import random

def problem2_6():
    """ Simulates rolling 2 dice 100 times """
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(431)  # don't remove when you submit for grading
    x = 0
    while x < 100:
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        print(str(a + b))
        x += 1

problem2_6()