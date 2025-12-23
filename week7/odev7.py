"""
import random
user = int(input("List Size: "))
list_type = input("Element Type: ")
list = []
for i in range(user):
    if list_type == "float":
         number = random.uniform(0, 999999)
         list.append(number)
    else:
         number = random.randint(0 , 999999)
         list.append(number)
print("Here is your random list you asked for:")
print(list)

def biggest_in_list(new_list: list):
    ans = max(my_list)
    return ans
def sorted_list(unsorted_list: list):
    ans = my_list[::-1]
    return ans
my_list = [695735, 169439, 41406, 112517, 457053]
print(my_list)
print(biggest_in_list(my_list))
print(sorted_list(my_list))

import random
def dice_roller(dice_type):
    ans = random.randint(1, dice_type)
    return ans
my_dice = int(input("Select dice: "))
print(f"{dice_roller(my_dice)}")

with open ("quote_from_bane.txt", "r") as my_file:
    content = my_file.read()
print(content)

user_input = int(input("Which line do you want to print? "))
with open("quote_from_bane.txt", "r") as my_file:
    line = my_file.readlines()
print(line[user_input - 1].strip())

def finder(file_name):
    with open(file_name, "r") as my_file:
        mylist = []
        for i in my_file:
            mylist.append(int(i.strip()))
        ans = max(mylist)
    return ans
print("Biggest is:", finder("random_numbers.txt"))

with open("single_line_data.csv", "r") as my_file:
    content = my_file.read()
    full_data = content.split(";")
name = full_data[0]
lucky_numbers = full_data[1:]
print("My Data:")
print(f"Name: {name}")
print(f"Lucky Numbers: {lucky_numbers}")

with open("new_file.txt", "w") as my_file:
    my_file.write("the quick brown fox jumps over the lazy dog")

import random
school_number = 240517021
with open("rand_list.txt", "w") as file:
    for i in range(1000):
        number = random.randint(0, school_number)
        file.write(str(number) + "\n")

text = "the quick brown fox jumps over the lazy dog"
with open("new_file.txt", "w") as file:
    for i in text.split():
        file.write(i + "\n")
"""
loop = True
while loop:
    user_input = input("Add or Exit: ")
    if user_input == "add":
        nickname = input("What is your nickname? ")
        score = input("What is your score? ")
        with open("high_scores.txt", "a") as file:
            file.write(f"Player name: {nickname} Score: {score}")
            file.write("\n")
            print("Score saved in high_scores.txt")
    else:
        loop = False
print("bye...")
