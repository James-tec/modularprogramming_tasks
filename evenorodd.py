class NumberChecker:

    def check_even_odd(self, num):

        if num % 2 == 0:

            print(num, "is even.")

        else:

            print(num, "is odd.")


checker = NumberChecker()

num = int(input("Enter a number: "))

checker.check_even_odd(num)

