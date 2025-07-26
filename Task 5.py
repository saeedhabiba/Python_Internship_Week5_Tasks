counter = 0  #global variable

def change_counter():
    global counter
    counter += 1

times = int(input("How many times do you want to update the counter? "))
for _ in range(times):
    change_counter()

print("Counter value is:", counter)