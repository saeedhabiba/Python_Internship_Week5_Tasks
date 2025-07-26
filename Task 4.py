def greet_user(name, age):
    return f"Hello {name}, you are {age} years old."

#taking input from user
name = input("Enter your name: ")
age = input("Enter your age: ")
print(greet_user(name, age))