"""
This program takes 10 numbers as input from the user, and display it in ascending order.
"""

num = [] # list to store numbers

for i in range(10): # loop to take 10 inputs
    while True:
        try:
            pass
        except ValueError:
            continue

print(f"Original numbers are: {num}") # print the original list
print(f"Numbers in ascending order are:") # print the result