<div align="center">

# One Dimensional Array: Number Array

</div>

---

## Ascending Order

### Overview

This program asks the user to enter 10 numbers, stores them in a list, and displays the numbers in ascending order. Input validation ensures only valid numbers are accepted.

### How the Code Works

#### 1. Input and Validation
```python
for i in range(10):
    while True:
        try:
            user_input = input(f"Enter number {i+1}: ")
            number = int(user_input)
            num.append(number)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
```
- Prompts the user for 10 numbers.
- Ensures each input is a valid integer before adding to the list.

#### 2. Bubble Sort Implementation
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

bubble_sort(num)
```
- Defines a `bubble_sort` function to sort the list in ascending order.
- Uses nested loops to repeatedly compare and swap adjacent elements if they are out of order.

#### 3. Output
```python
print(f"Ascending Order: {num}")
```
- Prints the sorted list after applying bubble sort.

---

## Positive Decimal Number to Binary

### Overview

This program converts a positive decimal number entered by the user into its binary equivalent, storing each binary digit in a list.

### How the Code Works

#### 1. Input and Validation
```python
user_num = int(input("Enter a positive decimal number: "))
if user_num > 0:
    temp = user_num
    # conversion process...
else:
    print("Please enter a positive integer.")
    exit()
```
- Prompts the user for a positive integer.
- Exits if the input is not positive.

#### 2. Conversion Logic
```python
while temp > 0:
    remainder = temp % 2
    binary.append(remainder)
    temp = temp // 2
binary.reverse()
```
- Repeatedly divides the number by 2, storing remainders in a list.
- Reverses the list to get the correct binary order.

#### 3. Output
```python
print("Binary equivalent:", end=" ")
for i in binary:
    print(i, end="")
```
- Prints the binary digits in order.

---

## Find Highest and Lowest (No Sorting)

### Overview

This program asks the user to enter 10 numbers and displays the 1st and 2nd highest and lowest numbers, without using array sorting.

### How the Code Works

#### 1. Input and Validation
```python
for i in range(10):
    while True:
        try:
            user_input = int(input(f"Enter number {i+1}: "))
            num.append(user_input)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
```
- Collects 10 valid integers from the user.

#### 2. Finding Highest and Lowest
```python
highest = second_highest = float('-inf')
lowest = second_lowest = float('inf')

for n in num:
    if n > highest:
        second_highest = highest
        highest = n
    elif n > second_highest and n != highest:
        second_highest = n

    if n < lowest:
        second_lowest = lowest
        lowest = n
    elif n < second_lowest and n != lowest:
        second_lowest = n
```
- Iterates through the list to find the highest, second highest, lowest, and second lowest values without sorting.

#### 3. Output
```python
print(f"1st highest number: {highest}")
print(f"2nd highest number: {second_highest}")
print(f"1st lowest number: {lowest}")
print(f"2nd lowest number: {second_lowest}")
```
- Displays the results to the user.

---

### Summary

- Each problem demonstrates array manipulation and input validation in Python.
- Sorting and searching are performed using explicit logic, not built-in shortcuts (except where allowed).
- The code is structured for clarity and user-friendly interaction.