# Ticket price calculator
age = int(input("What is your age? "))

if age < 0:
    print("Invalid age")
elif age < 5:
    print("Free")
elif age <= 17:
    print("10 pounds")
elif age <= 59:
    print("25 pounds")
else:
    print("15 pounds")
