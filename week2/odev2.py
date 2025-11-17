"""""
fahrenheit = float(input("Please type in a temperature (F): "))
celsius = ((fahrenheit - 32) * 5/9)
print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")
if celsius < 0:
    print ("Brr! It's cold in here!")

Hourly_wage = float(input("Hourly wage: "))
Hours_worked = float(input("Hours worked: "))
Day_of_the_week = input("Day of the week: ")
if Day_of_the_week == "sunday":
    daily_wage = (Hourly_wage * 2) * Hours_worked
else: daily_wage = Hourly_wage * Hours_worked
print(f"daily_wage: {daily_wage} liras")

old = int(input("How old are you? "))
if old >= 44:
    print("You are too old for this sh*t")
elif old < 18:
    print("You can't play Dark Souls")
else: print("Here is Dark Souls. Lol")

first_number = int(input("Type the first number: "))
second_number = int(input("Type the second one: "))
if first_number > second_number:
      print(f"First one is greater ({first_number}>{second_number})")
elif second_number > first_number:
      print(f"Second one is greater ({second_number}> {first_number})")
else:
    print(f"These are equal ({first_number}={second_number})")
    
first_word = input("Type the first number: ")
second_word = input("Type the second one: ")
if first_word < second_word:
    print(f"{second_word} comes alphabetically last")
elif first_word > second_word:
    print(f"{first_word} comes alphabetically last")
else:
    print("These are same!")

community = input("Which community do you belong to?: ")
if community == "New California Republic" or community == "Ncr" or community == "Brotherhood of Steel" or community == "Caesar’s Legion" or community == "Great Khans or community" == "Vault Dweller":
    print("You’re belong to Fallout Universe.")
else: 
    print("Nope, you are not belong to Fallout Lore")

points = int(input("How many points [0-100]: "))
if points < 0:
    print("Grade: you what?")
elif points >= 0 and points <= 49:
    print("Grade: fail")
elif points >= 50 and points <= 59:
    print("Grade: 1")
elif points >= 60 and points <= 69:
    print("Grade: 2")
elif points >= 70 and points <= 79:
    print("Grade: 3")
elif points >= 80 and points <= 89:
    print("Grade: 4")
elif points >= 90 and points <= 100:
    print("Grade: 5")
else:
    print("Grade: impossible!")

number = int(input("Enter number: "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")

number = int(input("Please type in a number: "))
if number > 0 and number % 2 == 0:
    print("The number is even")
elif number > 0 and number % 2 == 1:
    print("The number is odd")
else:
    print("The number is negative or zero")

year = int(input("Please type in a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")
    """