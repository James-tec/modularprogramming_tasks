class Calculator:

    def add_numbers(self, num1, num2):

        return num1 + num2


calculator = Calculator()

num1 = float(input("Enter first number: "))

num2 = float(input("Enter second number: "))

result = calculator.add_numbers(num1, num2)

print("The sum is:", result)

