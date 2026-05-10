import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
characters = ['!', '@', '#', '$', '%', '^', '&', '*','(', ')', ]

print("Welcome to the PyPassword Generator!\n")

user_letter = int(input("How many letters would you like in your password?\n"))
user_number = int(input("How many numbers would you like?\n"))
user_symbol = int(input("How many symbols would you like?\n"))

#Easier version

easy_password = ""

for letter in range(0, user_letter):
    easy_password += random.choice(letters)

for symbol in range(0, user_symbol):
    easy_password += random.choice(characters)

for number in range(0, user_number):
    easy_password += random.choice(numbers)

print(f"The easy password is: {easy_password}\n")

#Harder version

password_list = []

for letter in range(1, user_letter+1):
    password_list.append(random.choice(letters))

for symbol in range(1, user_symbol+1):
    password_list.append(random.choice(characters))

for number in range(1, user_number+1):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

hard_password = ""

for char in password_list:
    hard_password += char

print(f"\nThe hard password is: {hard_password}")