def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
#taking input from user
num = int(input("Enter a number to check if it's even or odd: "))
print("The number is", is_even_or_odd(num))