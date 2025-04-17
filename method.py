# METHOD BRANCH WOULD BE INSERTED

# Using a for loop to print numbers from 1 to 5 with "Good Morning"
for i in range(1, 6):
    print(f"{i}. Good Morning")

# Program to reverse a number

# Input from user
number = int(input("Enter a number: "))

# Initialize reversed number to 0
reversed_number = 0

# Reverse the number
while number != 0:
    digit = number % 10  # Get the last digit
    reversed_number = reversed_number * 10 + digit  # Append the digit to reversed number
    number = number // 10  # Remove the last digit from the original number

print(f"Reversed Number: {reversed_number}")
