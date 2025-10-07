"""
This program checks if a given word is a palindrome or not.
"""

import re

def is_palindrome(word):
    word_lower = word.lower()
    return word_lower == word_lower[::-1]

while True:
    word = input("Enter a word: ")
    if re.fullmatch(r"[A-Za-z]+", word):
        break
    else:
        print("Invalid input. Please enter letters only.")

if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")