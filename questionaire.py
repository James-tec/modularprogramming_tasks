import random


class MathQuiz:

    def generate_question(self):

        num1 = random.randint(1, 10)

        num2 = random.randint(1, 10)

        operator = random.choice(['+', '-'])

        if operator == '+':

            answer = num1 + num2

        else:

            answer = num1 - num2

        return num1, num2, operator, answer


    def check_answer(self, num1, num2, operator, answer):

        user_answer = int(input(f"What is {num1} {operator} {num2}? "))

        if user_answer == answer:

            print("Correct!")

        else:

            print("Incorrect. The correct answer is", answer)


quiz = MathQuiz()

for _ in range(5):

    num1, num2, operator, answer = quiz.generate_question()

    quiz.check_answer(num1, num2, operator, answer)

