"""
SimpleLoginSystem Program

This program takes a username and password from the user
and checks them against predefined credentials.
"""

# Take username input from the user
user_name = input("Enter user name: ")

# Take password input from the user
user_pass = input("Enter password: ")

# Check if entered credentials match the stored credentials
if (user_name == username) and (user_pass == password):
    # If both username and password match
    print("Login successful")
else:
    # If username or password is incorrect
    print("Invalid credentials")
