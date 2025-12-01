1. Context and Purpose-
Modern software development uses tools like VS Code, Git, and GitHub to make coding organized and professional.
This mini-project helps practice these skills by building a small application, managing it with Git, and hosting it online using GitHub.
 
2. Task Description -
Step 1 – Project Selection & Setup
Chosen Project: Basic Calculator in Python
Features: Addition, subtraction, multiplication, division
Setup Done Using:
•	Visual Studio Code (for writing and running code)
•	Git (for version control)
•	GitHub (to host the project)
Folder example:
calculator-project/
│── calculator.py
│── .gitignore
│── README.md
│── docs/
│     ├── overview.md
│     ├── development.md
│     ├── future.md
 
Step 2 – Use of Development Tools
Git Commands Used
Examples of the commits you can make:
1.	git init – initialized repository
2.	git add calculator.py
3.	git commit -m "Added basic arithmetic functions"
4.	git commit -m "Improved user input handling"
5.	git commit -m "Updated README with screenshots"
6.	git push origin main
You need at least 5 meaningful commits.
 
Step 3 – Documentation & Repository Structure
✔ .gitignore
Example entries:
.vscode/
__pycache__/
*.log
✔ README.md Should Include:
•	Project title
•	Description
•	How to install and run
•	Features
•	Screenshots
Easy Example Description:
This is a basic Python calculator that performs addition, subtraction, multiplication, and division. It is built using VS Code and maintained using Git & GitHub.
✔ docs/ Folder Contents:
1.	overview.md → brief explanation of the project
2.	development.md → how you built it (steps in VS Code, commits, testing)
3.	future.md → future features like GUI, history log, etc.
 
3. Expected Output 
By the end, your GitHub repository should include:
•	✔ Working Python calculator
•	✔ README with screenshots
•	✔ docs folder with markdown files
•	✔ Proper commits
•	✔ .gitignore file
 
4. Short Example Code for a Simple Python Calculator
You can use this as inspiration (rewrite it in your own words):
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Error! Division by zero."

print("Simple Calculator")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

choice = input("Enter choice (1-4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(add(num1, num2))
elif choice == '2':
    print(subtract(num1, num2))
elif choice == '3':
    print(multiply(num1, num2))
elif choice == '4':
    print(divide(num1, num2))
else:
    print("Invalid choice")
<img width="468" height="635" alt="image" src="https://github.com/user-attachments/assets/f62c66bb-e995-4a0b-bccc-ef1f35f72598" />


# screenshot also available. so check the repository
