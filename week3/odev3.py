"""""
def print_name(name):
    print(f"hello {name}")
user_input = input("Please input an argument: ")
print_name(user_input)

def print_name(name):
    return f"Hello {name}"
user_input = input("Please input an argument: ")
print_name = print_name(user_input)
print(print_name)

def sum(a,b):
    return a + b
print(sum(3, 2))

def greeting(input_name):
    print(f"Hi {input_name}")
greeting("Andrew Ryan")
greeting("Gordon Freeman")

def greeting(a,b,c):
    print((a + b + c)/3)
greeting(1,2,3)

Loop = True
while Loop:
    user_input = input("Say my name: ")
    if user_input == ("Heisenberg"):
        Loop = False
        print("You're goddamn right.")

password_loop = True
while password_loop:
    enter_password = input("Enter your password: ")
    enter_password_again = input("Enter again: ")
    if enter_password == enter_password_again:
            print("Your password matches and account created successfully")
    else:
           print("They are not same.")
    password_loop = False
    
user_number = int(input("Please enter a number: "))
while user_number > 0:
    print(f"{user_number}")
    user_number = user_number - 1
print("Kaboom")

attempts_remaining = 3
password = int("314159")
while attempts_remaining > 0:
    user_password = int(input("Password: "))
    if user_password == password:
        print("Welcome")
        attempts_remaining = 0
    else:
        if password != user_password:
            print("Try again")
            attempts_remaining = attempts_remaining - 1
            if attempts_remaining == 0:
                print("Incorrect Password. Exterminate...")

def dumb_calculator():
    print("dumb calculator v0.1 If you want to exit, enter 0")
    count = 0
    total_sum = 0
    odd_count = 0
    even_count = 0
    loop = True
    while loop:
        user_input = input("please enter a number: ")
        number = int(user_input)
        if number != 0:
            count = count + 1
            total_sum = total_sum + number
            if number % 2 == 0:
                even_count = even_count + 1
            else:
                odd_count = odd_count + 1
        else:
            loop = False
    if count > 0:
        arithmetic_mean = round(total_sum / count, 2)
    else:
        arithmetic_mean = 0
    print(f"Total Number: {count}")
    print(f"Sum: {total_sum}")
    print(f"Mean: {arithmetic_mean}")
    print(f"Odd: {odd_count} Even: {even_count}")
dumb_calculator()

my_list = []
my_list.append("my first Item")
my_list.append("my second item")
my_list.append("my last item")
print(my_list)
print(my_list[0])
print(f"List length is {len(my_list)}")
my_list.pop(1)
print(my_list)

my_list = []
my_list.append("my first item")
my_list.append("my second item")
my_list.append("my last item")
print(my_list)
my_list[0] = ("my new item")
print(my_list)

user_input = []
loop = True
while loop:
    user = input("Please enter an input: ")
    if user != ("exit"):
        user_input.append(user)
    else:
        print(user_input)

my_list = ["Mahmut", "Agent 47", "Kratos", "Geodude", "Heisenberg"]
for i in my_list:
    print(i)

user = input("Please enter an input: ")
for i in user:
    print(i)

raw_points = [1, 2, 1, 3]
total_points = 0
for point in raw_points:
    total_points = total_points + point
print(f"total {total_points} points earned")

raw_points = [1, -2, 1, 3, -5, 7, 0]
total_points = 0
for point in raw_points:
    if point > 0:
        total_points = point + total_points
print(f"total {total_points} points earned")

size = int(input("please input table size: "))
for i in range(size):
    print("|" + "_|" * size)
"""
height = int(input("Spruce height: "))
for i in range(1, height + 1):
    spaces = " " * (height - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
print(" " * (height - 1) + "*")
