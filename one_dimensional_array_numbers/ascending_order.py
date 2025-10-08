"""
This program takes 10 numbers as input from the user, and displays them in ascending order using bubble sort.
"""

# Function to perform bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

num = []  # list to store numbers

# Input loop to take 10 numbers from the user
for i in range(10):
    while True:
        try:
            user_input = input(f"Enter number {i+1}: ")  # take input from user
            number = int(user_input)
            num.append(number)  # append the number to the list
            break
        except ValueError: # invalid input
            print("Invalid input. Please enter a valid number.")

bubble_sort(num)  # sort the list in ascending order using bubble sort

print(f"Ascending Order: {num}")  # print the sorted list