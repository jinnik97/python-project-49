import random

DESCRIPTION = 'What is the result of the expression?'

OPERATORS = ['+', '-', '*']


def calculate(number1, number2, operator):
    match operator:
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case '*':
            return number1 * number2
        

def generate_round():  
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operator = random.choice(OPERATORS)

    question = f'{number1} {operator} {number2}'

    result = str(calculate(number1, number2, operator))

    return question, result