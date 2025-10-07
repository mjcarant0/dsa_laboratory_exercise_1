"""
This program asks the user to enter a positive decimal number and converts it to its equivalent binary number
"""

user_num = int(input("Enter a positive decimal number: "))
binary = []  # to store binary digits

if user_num > 0: # check if the number is positive
    temp = user_num  # temporary store the original input

    # conversion process
    while temp > 0:
        remainder = temp % 2  # find remainder
        binary.append(remainder)
        temp = temp // 2  # update temp by dividing it by 2
    binary.reverse()  # reverse the list to get the correct binary representation

    # print the binary equivalent
    print("Binary equivalent:", end=" ")
    for i in binary:
        print(i, end="") 

else: # handle non-positive input
    print("Please enter a positive integer.")
    exit()