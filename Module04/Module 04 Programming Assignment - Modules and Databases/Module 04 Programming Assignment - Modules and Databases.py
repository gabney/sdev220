"""
Module 04 Programming Assignment - Modules and Databases
SDEV 220 Software Development Using Python
Gabriel Abney

This assignment asks us to complete specific exercises from our textbook \
found at the end of the chapters 11 and 16.  Specifically, the exercises \
11.1 and 11.2 from chapter 11, and 16.8 from chapter 16.

My work for these exercises can be found in the program below.
Additionally, the prompt for each exercise is commented above my work.
"""



# 11.1 Create a file called zoo.py. In it, define a function called hours() \
# that prints the string 'Open 9-5 daily'. Then, use the interactive interpreter \
# to import the zoo module and call its hours() function.

# note: see the additional file in the assignment folder called zoo.py 

#imports zoo package
import zoo

#calls hours function defined in zoo package
zoo.hours()




# 11.2 In the interactive interpreter, import the zoo module as menagerie \
# and call its hours() function.

# imports zoo package as 'menagerie'
import zoo as menagerie

#calls the hours function with the name menagerie
menagerie.hours()




