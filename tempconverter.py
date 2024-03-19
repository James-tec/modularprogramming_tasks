class TemperatureConverter:

    def celsius_to_fahrenheit(self, celsius):

        return (celsius * 9/5) + 32


converter = TemperatureConverter()

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = converter.celsius_to_fahrenheit(celsius)

print("Temperature in Fahrenheit:", fahrenheit)

