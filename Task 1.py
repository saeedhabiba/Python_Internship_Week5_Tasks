def square_numbers(numbers):
    squared = []
    for num in numbers:
        squared.append(num ** 2)
    return squared

#taking input from user
user_input = input("Enter numbers separated by commas: ")
num_list = [int(x.strip()) for x in user_input.split(',')]
print("Squares:", square_numbers(num_list))