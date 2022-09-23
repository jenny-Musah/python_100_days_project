print("Welcome to python Pizza Deliveries")
bill = 0
size = input("What size of pizza do you want S, M or L ?")
pepperoni = input("Do you want pepperoni? Y Or N ?")
if size == "S" or "s":
    bill = 15
    if pepperoni == "Y" or "y":
        bill += 2
elif size == "M" or "m":
    bill = 20
    if pepperoni == "Y" or "y":
        bill += 3
elif size == "L" or "l":
    bill = 25
    if pepperoni == "Y" or "y":
        bill += 3
extra_chess = input("Do you want extra chess? Y or N ?")
if extra_chess == "Y" or "y":
    bill += 1

print(f"Your finial bill is: {bill}")
