## Grade tracker
### Project overview
Grade Tracker is a  Python program that allows the user to create and track his or her academic assignments and grades.

The program allows the user to create homework and exams, view saved assignments, filter assignments, and create an overview of his/her academic results.

This project includes such Python concepts as object-oriented programming, inheritance, functions, loop, conditional statements, lists, dictionaries, input validation, and error handling.

## Features

The Grade Tracker allows the user to:

- Create homework assignments
- Create exam assignments
- List all assignments
- Filter assignments by subject
- Filter assignments by type of assignment
- Filter assignments by month
- Get grade average
- Get grade average by subject
- Find best score assignment
- Find worst score assignment
- Validate user input
- Terminate the program
## Structure of Project

The project consists of the following main Python files:

### assignment.py

Includes the assignment classes:

- `Assignment` – parent class which holds common information about assignments.
- `Homework` – child class for holding information about homework assignments.
- `Exam` – child class for holding information about exam assignments.

### tracker.py

Includes `GradeTracker` class.

This class is responsible for managing the collection of assignments and performing the following actions:

- adding assignments;
- listing assignments;
- filtering assignments;
- calculating grade summary.

### indexx.py

Includes the main program and user interface.

It shows the Grade Tracker menu, receives the user input, checks it and connects the user with the functions of `GradeTracker` class.

## Running the Program

1. Install Python on your computer.

2. Clone the project repository.
3. Open the program folder in VS Code or any other Python code editor.

4. Open a terminal window inside the program folder.

5. Enter:
py main.py
 ## Main Menu

At the start of the application, the following menu appears:

=================================
          GRADE TRACKER
=================================
1. Enter Homework
2. Enter Exam
3. List Assignments
4. Search Assignments
5. Print Summary
0. Quit
=================================

Input the corresponding number for your required task.

Example Assignment

An example of the assignment that can be input by a user is:

Subject: Programming
Title: Python Functions
Score: 18
Maximum Score: 20
Deadline: 2026-08-20

The percentage will be calculated by the application.

In this case:
Percentage: 90.00%

## Filtering 

The assignments can be filtered based on:

Subject 
Assignment type (Homework or Exam) 
Month in the YYYY-MM format 

Example: 
2026-08

This will show you assignments due in the month of August 2026. 

## Grade Summary 

This feature shows:

Overall average 
Average per subject 
Highest scoring assignment 
Lowest scoring assignment 
Input Validation

The program checks for valid user input.

Some examples of invalid input include:
Empty subjects or assignment titles
Negative scores
Scores greater than the maximum score
Maximum scores of zero or less
Non-numeric scores
Incorrect date formats
Invalid menu selections

Dates must use the following format:
YYYY-MM-DD

For example:
2026-08-20

## Data Storage

Information about assignments is stored in memory throughout the program session.

The application doesn’t have any database or file where it can store the assignments permanently. Thus, all assignments get deleted once the program is terminated.

Python Concepts Illustrated

The current project illustrates the following concepts of Python programming:

Variables and datatypes
Strings
Conditionals
Loops
Functions
Lists
Dictionaries
Classes and Objects
Inheritance
Exception Handling
Input Validation

## Author
Angelica Bukari