class DigitSummer:

    def sum_of_digits(self, number):

        total = 0

        while number > 0:

            total += number % 10

            number //= 10

        return total


summer = DigitSummer()

num = int(input("Enter a number: "))

print("Sum of digits:", summer.sum_of_digits(num))

