"""
Module 2 Lab - Case Study IF ELSE and WHILE
Gabriel Abney
SDEV 220

This program accepts user input for a last name, first name, and 
GPA for a hypothetical student.  If last name entered is ZZZ, exits
the program.  Otherwise, the program checks the GPA to see if the student 
made Dean's List (GPA above 3.5) or Honor ROll (GPA above 3.25) and 
prints this information out to the user.
"""

#variables and explanations
lastname = "" #student last name
firstname = "" #student first name
GPA = "" #student GPA, stored as a float


#main body loop
while True:
    print("Welcome to ACME grade processing program.") #program start statement
    lastname = input("Please enter student's last name, or type 'ZZZ' to exit: ") #accepts input for last name
    if lastname == "ZZZ": #exits loop if sentinel value is entered, ending program
        print("Closing program. Goodbye!")
        break
    else:
        firstname = input("Please enter student's first name: ") #accepts first name input
        GPA = float(input("Please enter student's GPA: ")) #accepts GPA input and converts to a float
        if GPA >= 3.5: #checks if GPA is equal to or greater than 3.5 and prints a message if so
            print(f"{firstname} {lastname} made the Dean's List. Congratulations!")
        elif GPA >= 3.25: #checks if GPA is equal to or greater than 3.25 and prints a message if so
            print(f"{firstname} {lastname} made the Honor Roll. Well done.")
        else: #if GPA is below 3.25, prints neutral message
            print(f"{firstname} {lastname} didn't earn any academic awards.")
        print("Returning to home screen.") #statement showing that program is returning to main loop body
