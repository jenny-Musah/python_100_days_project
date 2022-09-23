print("Welcome to tip calculator")
bill = float(input("What is the total bill? $"))
percentage_tip = int(input("What percentage tip would like to give 10, 12 or 15?")) / 100 + 1
number_of_people_to_split_bill = int(input("How many people are to split the bill?"))
tip = (percentage_tip * bill) / number_of_people_to_split_bill
print(f"Each person should pay {round(tip,2)}")
