# Simple login system
user_name = input("What is your user name? ").lower()
password = input("Enter your password: ")

if user_name == "hanaa" and password == "Hana0":
    print("Welcome back!")
elif user_name == "hanaa":
    print("Password is not correct")
else:
    print("User not found")
