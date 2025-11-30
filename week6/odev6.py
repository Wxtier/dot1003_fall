"""""
def coordinator(x, y):
    return x, y 
my_coordinates = coordinator(5, 6)
print(my_coordinates)

my_coordinates = {}
def coorditanor(x,y):
    return x, y
my_coordinates[coorditanor(0,0)] = "Home"
my_coordinates[coorditanor(1,1)] = "Work"
my_coordinates[coorditanor(-1,-1)] = "School"
for k,v in my_coordinates.items():
    print(f"position: {k} name: {v}")

weapon1 = ("blade", 10,)
weapon2 = ("sabre", 35)
weapon3 = ("sword", 50)
meele_weapon = [weapon1, weapon2, weapon3]
def print_best_weapon(weapon_list):
    best_weapon_name = ""
    max_damage = 0
    for weapon_tuple in weapon_list:
        current_name = weapon_tuple[0]
        current_damage = weapon_tuple[1]
        if current_damage > max_damage:
            max_damage = current_damage
            best_weapon_name = current_name
    print(best_weapon_name)
print_best_weapon(meele_weapon)

game_table = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
user_inputs = []
def coordinator(x, y):
    return x, y 
loop = True
while loop:
    command = input("please type new or exit: ")
    if command == "exit":
        loop = False
    elif command == "new":
        x = int(input("please enter x: ")) 
        y = int(input("please enter y: "))
        new_coordinate = coordinator(x, y)
        user_inputs.append(new_coordinate)
for coord in user_inputs:
    x = coord[0]
    y = coord[1]
    game_table[x][y] = "*"
for row in game_table:
    print("_".join(row))

my_set = set()
loop = True
while loop:
    user_input = input("Enter an element for set: ")
    if user_input == "exit":
        loop = False
    else:
        my_set.add(user_input)
for item in my_set:
    print(item)

def ask_name(): 
    my_ans = "" #local
    return input("Please enter a character from Lord of the Rings")
def ask_age():
    my_ans = int(input(f"How old are {name}: ")) #local
    return my_ans
real_age = 55000 #global
name = ask_name() #global
question = f"Here is the questions about {name}" #global
print("")
user_guess = ask_age() #global
if real_age == user_guess:
    my_ans = "You’re Right" #global
    print(my_ans)
else:
    print("Nope")
"""
def start_game():
    global score
    score = 10
    print(f"Game started! Current score: {score}")
def increase_score():
    global score
    score += 5
    print(f"Score increased! Current score: {score}")
def display_score():
    print(f"Final score: {score}")
score = 0
start_game()
increase_score()
display_score()