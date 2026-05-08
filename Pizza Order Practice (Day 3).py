import random
print("Welcome to Pizza Order Deliveries!")

size = input("What size of pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

colleagues = ["Rahnuma", "Eva", "Mithyla", "Raka", "Tasnim", "Effat", "Rokeya", "Ripa"]
bill_pay = random.choice(colleagues)
price = 0

if size == "S":
    price = 15
    if pepperoni == "Y":
        price += 2
elif size == "M":
    price = 20
    if pepperoni == "Y":
        price += 3
elif size == "L":
    price =25
    if pepperoni == "Y":
        price += 3
else:
    print("You types the wrong input.")

if extra_cheese == "Y":
    price += 1

print(f"Your final bill is ${price} and the bill will be paid by {bill_pay}.")


