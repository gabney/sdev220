"""
Module 03 Programming Assignment - Lists and Functions
SDEV 220
Gabriel Abney

This program contains my work for the series of exercises in \
our textbook for the module 03 programming assignment.  The \
exercises are 7.4, 7.5, 7.6, 7.7, 9.1, and 9.2 . 

The instructions for each exercise are commented out directly \
above my work to complete them.
"""


# exercise 7.4
# Make a list called things with these three strings as \
# elements: "mozzarella", "cinderella", "salmonella".

things = ["mozzerella", "cinderella", "salmonella"]
print(things)


# exercise 7.5
# Capitalize the element in things that refers to a person \
# and then print the list. Did it change the element in the list?

things[1] = things[1].capitalize()
print(things) # Yes, the element was changed in the list because I assigned the capitalized word


# exercise 7.6
# Make the cheesy element of things all uppercase and then print the list.

# I tried (and succeeded) using the index to search the list for its occurrence rather than specifying a location in the list
things[things.index("mozzerella")] = things[things.index("mozzerella")].upper() 
print(things)


# exercise 7.7 
# Delete the disease element from things, collect your Nobel Prize, and print the list.

things.remove("salmonella")
print(things)


# exercise 9.1
# Define a function called good() that returns the following \
# list: ['Harry', 'Ron', 'Hermione'].
def good():
    return ["Harry", "Ron", "Hermione"]

print(good())


# exercise 9.2
# Define a generator function called get_odds() that returns the odd numbers \
# from range(10). Use a for loop to find and print the third value returned.

def get_odds(odds_range = 10): # generator function creation, with default value of 10
    for odd in range(odds_range):
        if odd % 2 != 0: #c heck to see if odd
            yield odd # yields the odd value

odd_gen = get_odds(10) # generator object
odd_gen_count = 0 # iteration tracking used in for loop below

for i in odd_gen:
    odd_gen_count += 1 
    if odd_gen_count == 3: #finds third iteration
        print(i)