"""
Module 02 Programming Assignment - Loops and Conditionals
Gabriel Abney
SDEV 220

This program contains my work from the series of exercises in \
our textbook for Module 02.  The exercises are: 4.1, 4.2, 6.1, \
6.2, and 6.3 .
The individual exercise instructions are commented out directly \
above my work to complete them.
"""

#exercise 4.1
# Choose a number between 1 and 10 and assign it to the variable secret. \
# Then, select another number between 1 and 10 and assign it to the variable guess. \
# Next, write the conditional tests (if, else, and elif) to print the string 'too low' \
# if guess is less than secret, 'too high' if greater than secret, and 'just right' if equal to secret.

secret = 5 #secret value
guess = 1 #inputted value, determined in advance for this exercise

if guess <= secret:
    print("Too low!")
elif guess >= secret:
    print("Too high!")
else:
    print("Just right!")


#exercise 4.2
#Assign True or False to the variables small and green. Write some if/else statements \
#to print which of these matches those choices: cherry, pea, watermelon, pumpkin.

small = True
green = False

if small == True:
    if green == True:
        print("It's a pea.")
    else:
        print("It's a cherry")
else:
    if green == True:
        print("It's a watermelon.")
    else:
        print("It's a pumpkin.")


#exercise 6.1
#Use a for loop to print the values of the list [3, 2, 1, 0].

my_list = [3, 2, 1, 0]
for i in my_list:
    print(i)


#exercise 6.2
# Assign the value 7 to the variable guess_me, and the value 1 to the variable number. \
# Write a while loop that compares number with guess_me. Print 'too low' if number is \
# less than guess me. If number equals guess_me, print 'found it!' and then exit the loop. \
# If number is greater than guess_me, print 'oops' and then exit the loop. Increment number \
# at the end of the loop.

guess_me = 7
number = 1

while True:
    if number < guess_me:
        print("Too low!")
    elif number == guess_me:
        print("Found it!")
        break
    else:
        print("Oops.")
        break
    number += 1


#exercise 6.3
#Assign the value 5 to the variable guess_me. Use a for loop to iterate a variable \
# called number over range(10). If number is less than guess_me, print 'too low'. \
# If it equals guess_me, print found it! and then break out of the for loop. \
# If number is greater than guess_me, print 'oops' and then exit the loop.

guess_me = 5

for number in range(10):
    if number < guess_me:
        print("Too low.")
    elif number == guess_me:
        print("Found it!")
        break
    else:
        print("Oops.")
        break