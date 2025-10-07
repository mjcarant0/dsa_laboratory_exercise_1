<div align="center">

# One Dimensional Array: Array of Characters

</div>

---

## Palindrome Checker

### Overview

This program checks if a given word is a palindrome—a word that reads the same forwards and backwards (e.g., "level", "radar"). It ensures the user inputs only alphabetic characters and provides clear feedback on whether the entered word is a palindrome.

---

### How the Code Works

#### 1. **Importing the `re` Module**
```python
import re
```
The `re` module (regular expressions) is imported to help validate that the user's input contains only letters.

---

#### 2. **Defining the Palindrome Checker Function**
```python
def is_palindrome(word):
    word_lower = word.lower()
    return word_lower == word_lower[::-1]
```
- **Purpose:** Checks if a word is a palindrome.
- **How:**  
  - Converts the input word to lowercase to make the check case-insensitive.
  - Compares the lowercase word to its reverse (`word_lower[::-1]`).
  - Returns `True` if they are the same, `False` otherwise.

---

#### 3. **User Input and Validation**
```python
while True:
    word = input("Enter a word: ")
    if re.fullmatch(r"[A-Za-z]+", word):
        break
    else:
        print("Invalid input. Please enter letters only.")
```
- **Purpose:** Ensures the user enters a valid word (letters only, no numbers or symbols).
- **How:**  
  - Prompts the user to enter a word.
  - Uses `re.fullmatch(r"[A-Za-z]+", word)` to check if the input contains only alphabetic characters.
  - If valid, breaks out of the loop.
  - If invalid, prints an error message and asks again.

---

#### 4. **Palindrome Check and Output**
```python
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
```
- **Purpose:** Tells the user if their word is a palindrome.
- **How:**  
  - Calls the `is_palindrome` function with the validated input.
  - Prints a message indicating whether the word is a palindrome.

---

### Summary

- The program validates user input to accept only words made of letters.
- It uses a function to check for palindromes in a case-insensitive way.
- The user receives clear feedback based on their input.