
"""
print("Whistling their whims on a low fence-wire")
print("And not one will know of the war")
print("not one")

haftadagün= 7
gündesaat= 24
saattedakika= 60
dakikadesaniye= 60
hoursinaweek= haftadagün * gündesaat
minutesinaweek = hoursinaweek * saattedakika
secondsinweek= minutesinaweek * dakikadesaniye
print("Hours in a week:")
print(f"{hoursinaweek}")
print("minutes in a week:")
print(f"{minutesinaweek}")
print("seconds in a week:")
print(f"{secondsinweek}")


name = input ("what is your name?")
print("What is your name? " + name)
email = input ("What is your email address?")
print("What is your email address? " + email)
nickname = input ("What is your nickname?")
print("What is your nickname? " + nickname)
print("Your name: " + name)
print("Your email address: " + email)
print("Your nickname: " + nickname)
print(name + email + nickname)


name = input("Name:")
victim = input("victim:")
print(f"Thank you,  {name1}")
print(f"But our {victim} is in another castle!")


name = "Courier"
age = 34
city = "New Vegas"
print(f"Hi {name}, you are {age} old. You live im {city}.")


name = "Ozan Akyol"
age = 18
skill1 = "python"
level1 = "beginner"
skill2 = "2d art"
level2 = "beginner"
lower = 2000
upper = 3000
print(f"My name is {name}, I am {age} years old ")
print()
print("My skills are")
print(f"- {skill1} ({level1})")
print(f"- {skill2} ({level2})")
print()
print(f"My salary expectation is {lower}-{upper} euros/month")


number1 = 3
number2 = 5
print(f"number 1 is: {number1}")
print(f"number 2 is: {number2}")
print()
top = (number1 + number2)
print(f"3 + 5 = {top}")
çık = (number1 - number2)
print(f"3 - 5 = {çık}")
çarp = (number1 * number2)
print(f"3 * 5 = {çarp}")
böl = (number1 / number2)
print(f"3 / 5 = {böl}")


height_str = input("Enter your weight: ")
weight_str = input("Enter your height: ")
height_m = float(height_str) / 100
weight_kg = float(weight_str)
BMI = weight_kg / (height_m ** 2)
print()
print(f"Your BMI is {BMI}")


oyun_isim = input("Game name: " )
çıkış = input("Which year was this game released? ")
çıkış_sayı = int(çıkış)
yıl = 2025
oyun_yaşı = yıl - çıkış_sayı
print()
print(f"{oyun_isim} is {oyun_yaşı} years old.")

number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))
işlem = number1 * number2 * number3
print(f"The product is {işlem}")


times = int(input("How many times a week do you eat at the student cafeteria? "))
price = int(input("The price of a typical student lunch? "))
groceries = int(input("How much money do you spend on groceries in a week? "))
cafeteria_weekly = times * price 
weekly_total = cafeteria_weekly + groceries
daily_average = weekly_total / 7
monthly_total = weekly_total * (30 / 7)
print()
print("Average food expenditure: ")
print(f"Daily: {daily_average} liras")
print(f"Weekly: {weekly_total} liras")
print(f"Montly: {monthly_total}")
"""""