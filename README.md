# Python Daily Practice

This repository contains my daily Python coding exercises.  
The goal is to write a small Python program every day to practice programming fundamentals and improve problem-solving skills.

---

## Day 1: Even or Odd Checker

**Description:**  
A simple Python program that asks the user to enter a number and tells whether the number is **Even** or **Odd**.

**What you learn:**  
- Taking input from the user using `input()`  
- Using `int()` to convert string input to integer  
- Using `if-else` statements  
- Using the modulus operator `%` to find remainder  

**Code Example:**

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")
