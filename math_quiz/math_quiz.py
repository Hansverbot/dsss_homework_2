import random
import keyboard


def random_number(min, max):
    """
    This function returns  a random number

    Args:

    min: lowest possible answer that  can be returned

    max: lowest possible answer that  can be returned

    return:

    random number

    """
    return random.randint(min, max)


def random_operator():

    """
    This function return one of three possible operators randomly

    """
    return random.choice(['+', '-', '*'])


def create_function(n1, n2, o):

    """
    It creates a function with the given arguments.

    Args:

    n1 = first number
    n2 = second number
    o = operator

    return: Returns p the function as a string and also gives back the answer in a number a.
    """
    p = f"{n1} {o} {n2}"
    if o == '+':
        a = n1 + n2
    elif o == '-':
        a = n1 - n2
    else:
        a = n1 * n2
    return p, a

def math_quiz():
    points = 0
    numberOfTries=3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(numberOfTries):
        n1 = random_number(1, 10);
        n2 = random_number(1, 5);
        o = random_operator()

        PROBLEM, ANSWER = create_function(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")

        while True: #Repeat until a valid answer
            try:
                useranswer = input("Your answer: ") #answer of the user as a string
                useranswer = int (useranswer) #convert into int
                break   #break if the answer is valid
            except ValueError:
                print("Please return an Integer! <3") #Return if input is wrong and not a valid number
            

        if useranswer == ANSWER: #compares the answer of the user to the correct one
            print("Correct! You earned a point.")
            points += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.") #Displays the correct answer if the user was wrong

    print(f"\nGame over! Your score is: {points}/{numberOfTries}") #Returns the score of the user

if __name__ == "__main__":
    math_quiz()
