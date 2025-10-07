"""
This program takes 10 numbers as input from the user, and display it in ascending order.
"""

num = [] # list to store numbers

for i in range(10): # loop to take 10 inputs
    while True:
        try:
            user_input = input(f"Enter number {i+1}: ") # take input from user
            numbers = int(user_input)
            num.append(numbers) # append the number to the list
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

num.sort() # sort the list in ascending order

print(f"Ascending Order: {num}") # print the sorted list