# Odd-Even-Number-Checker
A simple Python mini-project that checks whether a given number is odd or even. 

A simple Python mini-project that checks whether a given number is odd or even.  
This project is part of my programming learning journey and uses **variables**, **data types**, **operators**, **if-else conditions**, **loops**, and **input/output**.

---

## 📌 Features
- Checks if a number is odd or even
- Allows repeated checking without restarting the program
- User-friendly and simple interface
- Written in pure Python

---

## 🛠️ Technologies Used
- Python 3.x

---

## 🚀 How to Run
1. Install Python on your system (if not already installed)  
2. Download the `odd_even_checker.py` file  
3. Run the file in the terminal or command prompt:
   ```bash
   python odd_even_checker.py

Welcome to the Odd & Even Checker
Enter a number: 4
4 is Even
Want to check again? (Han/Na): han
Enter a number: 7
7 is Odd
Want to check again? (Han/Na): na
Thanks for using the program!

🎯 Learning Objectives
Understand basic input/output in Python

Practice if-else decision making

Work with loops for repeated execution

Learn how to use the modulus operator (%)

📬 Connect With Me
LinkedIn: www.linkedin.com/in/ashar-khanzada-549b5a354

python

## **2️⃣ odd_even_checker.py (Python file)**
```python
# Odd and Even Number Checker
# Author: Ashar Khanzada
# Date: 2025-08-09
# Description: A mini-project to check if a number is odd or even.

print("Welcome to the Odd & Even Checker")

while True:
    # Take input from the user
    digit = int(input("Enter a number: "))

    # Check if the number is even or odd
    if digit % 2 == 0:
        print(f"{digit} is Even")
    else:
        print(f"{digit} is Odd")

    # Ask user if they want to check again
    digit_1 = input("Want to check again? (Han/Na): ").strip().lower()
    if digit_1 == "na":
        print("Thanks for using the program!")
