"""""
my_list = ("The quick brown fox jumps over the lazy dog")
user_input = input("Which item do you want to search? ")
count = my_list.count(user_input)
print(f"item {user_input} appeared {count} times")

def Game_of_the_Year():
    input_search = input("Enter the input to search: ")
    item_search = input("Which item do you want to search?: ")
    count = input_search.count(item_search)
    print(f"item {item_search} appeared {count} times")
Game_of_the_Year()

def clear_vowels(text):
    vowels = "aeiouAEIOU"
    new_text = ""
    for char in text:
        if char not in vowels:
            new_text += char
    return new_text

menu_button = "new game"
print(clear_vowels(menu_button))
def anarya(liste):
    return liste[::-1]
game_list = ["Doom", "Max Payne", "FTL"]
print(game_list)
print(anarya(game_list))

def finder(element):
    for row in my_matrix:
        print(row)
    print(finder(my_matrix,element))
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]

def sum_of_row(matrix, row_no):
    return sum(matrix[row_no])
my_matrix = [[1,2,3], [4,5,6], [7,8,9]]
element = int(input("row no: "))
print(my_matrix[0])
print(my_matrix[1])
print(my_matrix[2])
result = sum_of_row(my_matrix, element)
print(result)

def sum_of_column(matrix, column_no):
    total_sum = 0
    for row in matrix:
        total_sum += row[column_no]
    return total_sum
my_matrix = [[1,2,3], [4,5,6], [7,8,9]]
element = int(input("column no: "))
for row in my_matrix:
    print(row)
result = sum_of_column(my_matrix, element)
print(result)

my_lucky_numbers = [4,8,15,16,23,42]
def tripler(input_list):
    new_list = [item * 3 for item in input_list]
    return new_list
tripled_numbers = tripler(my_lucky_numbers)
print(f"My Lucky Numbers: {my_lucky_numbers}")
print(f"Tripled Numbers: {tripled_numbers}")

inventory = {}
inventory["item1"] = 3
inventory["item2"] = 1
inventory["item3"] = 5
for item, quantity in inventory.items():
    print(f"{item}: {quantity}")

inventory = {}
inventory["item1"] = 3
inventory["item2"] = 1
inventory["item3"] = 5
def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
add_item("item1", 5)
add_item("item4", 1)
for key, value in inventory.items():
    print(key + ":", value)

inventory = {}
inventory["item1"] = 3
inventory["item2"] = 1
inventory["item3"] = 5
def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
def remove_item(item, quantity):
    if item in inventory:
        current_quantity = inventory[item]
        if current_quantity < quantity:
            inventory[item] = 0
        else:
            inventory[item] -= quantity
add_item("item1", 5)
add_item("item4", 1)
remove_item("item4", 6)
remove_item("item1", 2)
for item, quantity in inventory.items():
    print(f">{item}: {quantity}")

inventory = {}
inventory["item1"] = 3
inventory["item2"] = 1
inventory["item3"] = 5
def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
def remove_item(item, quantity):
    if item in inventory:
        current_quantity = inventory[item]
        if current_quantity < quantity:
            del inventory[item]
        else:
            inventory[item] -= quantity
            new_quantity = inventory[item]
            if new_quantity == 0:
                del inventory[item]
add_item("item1", 5)
add_item("item4", 1)
remove_item("item4", 6)
remove_item("item1", 2)
for item, quantity in inventory.items():
    print(f">{item}: {quantity}")
"""