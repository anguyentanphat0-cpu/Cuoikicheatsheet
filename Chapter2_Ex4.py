
celsius_str = input('Enter Celsius temperature: ')
try:
    celsius = float(celsius_str)
except ValueError:
    print('Invalid input. Please enter a number.')
    quit()
fahrenheit = (celsius * 9/5) + 32
print('The temperature in Fahrenheit is:', fahrenheit)