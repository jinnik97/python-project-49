import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(start, step, length):
    progression = []

    for index in range(length):
        current_element = start + index * step

        progression.append(current_element)

    return progression


def generate_round():
    start = random.randint(1, 100)
    length = random.randint(5, 10)
    step = random.randint(2, 10)

    index = random.randrange(length)

    numbers = generate_progression(start, step, length)

    correct_answer = str(numbers[index])

    numbers[index] = '..'

    question = ' '.join(map(str, numbers))

    return question, correct_answer