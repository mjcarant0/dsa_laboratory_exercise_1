"""
This program finds the 1st and 2nd highest and lowest user's input numbers
"""

num = [] # to store user input

for i in range(10): # loop to take 10 inputs from user
    while True:
        # Input validation to ensure the user enters an integer 
        try:
            user_input = int(input(f"Enter number {i+1}: "))
            num.append(user_input)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Initialize variables for highest and lowest
highest = second_highest = float('-inf')
lowest = second_lowest = float('inf')

for n in num:
    # Find highest and second highest
    if n > highest:
        second_highest = highest
        highest = n
    elif n > second_highest and n != highest:
        second_highest = n

    # Find lowest and second lowest
    if n < lowest:
        second_lowest = lowest
        lowest = n
    elif n < second_lowest and n != lowest:
        second_lowest = n

print()
print(f"1st highest number: {highest}")
print(f"2nd highest number: {second_highest}")
print(f"1st lowest number: {lowest}")
print(f"2nd lowest number: {second_lowest}")