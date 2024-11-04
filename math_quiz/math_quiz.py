import random


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
    p = f"{n1} {o} {n2}"
    if o == '+':
        a = n1 + n2
    elif o == '-':
        a = n1 - n2
    else:
        a = n1 * n2
    return p, a

def math_quiz():
    start = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = random_number(1, 10);
        n2 = random_number(1, 5.5);
        o = random_operator()

        PROBLEM, ANSWER = create_function(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
