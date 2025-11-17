"""""
repetition = int(input("How many repetition for li: "))
city_name = input("Which word: ")
li_rep = repetition * "li"
combined_word = city_name + li_rep + "lerle"
print(combined_word)
"
def word():
    firs_word = input("First Word: ")
    second_word = input("Second Word: ")
    firs_word_lenght = len(firs_word)
    second_word_lenght = len(second_word)
    if firs_word_lenght > second_word_lenght:
        print(firs_word)
    elif second_word_lenght > firs_word_lenght:
        print(second_word)
    else:
        print("Their length are same")
word()

def print_with_stars():
    user_input = input("Your Input: ")
    print(f"*{user_input}*")
print_with_stars()

def dynamic_underline():
    user_input = input("Your Input: ")
    text_length = len(user_input)
    print(user_input)
    print(text_length * "-")
dynamic_underline()

def programming_task():
    max_len = 18
    user_input = input("Your Input: ")
    total_missing = max_len - len(user_input)
    left_missing = total_missing // 2
    right_missing = total_missing - left_missing
    if total_missing > 0:
        result = (">" * left_missing) + user_input + ("<" * right_missing)
    else:
        result = user_input[:18]
    print("------------------")
    print("|" + result + "|")
    print("------------------")
programming_task()

string = input("Please enter string: ")
integer1 = int(input("Please enter first integer: "))
integer2 = int(input("Please enter last integer: "))
print(string[integer1:integer2])

string = input("Please enter string: ")
integer = int(input("Please enter first integer: "))
print(string[0:integer])

string = input("Please enter string: ")
integer = int(input("Please enter first integer: "))
print(string[integer:])

user_string = input("Please enter string: ")
if "a" in user_string:
    print("found")
else:
    print("not found")

user_string = input("Please enter string: ")
user_search = input("Please enter search item: ")
if user_search in user_string:
    print("found")
else:
    print("not found")

user_string = input("Please enter string: ")
user_search = input("Please enter search item: ")
if user_search in user_string:
    print(f"found it at {user_string.find(user_search)}")
else:
    print("not found")

sentence = ("The quick brown fox jumps over the lazy dog")
user_search = input("What are you looking for? ")
if user_search in sentence:
    print(f"found it at {sentence.find(user_search)}")
elif user_search == "-1":
    print("Bye.")
else:
    print("not found")
"""
def to_two_decimal(numbers):
    new_list = []
    for number in numbers:
        new_list.append(f"{number:.2f}")
    return new_list
my_list = [1.2345, 2.3456, 3.4567, 4.5678]
new_list = to_two_decimal(my_list)
print(new_list)