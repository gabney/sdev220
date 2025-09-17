"""
Module 03 Tutorial - Functional vs OOP Programming
SDEV 220
Gabriel Abney

This program contains my work from the two programming exercises \
from Module 3.  
The first exercise, "Sort an Array of 0s, 1s, and 2s", has us develop \
a sorting mechanism without using the Python sort() method to arrange \
the data in a list to be sorted numerically.  This is accomplished by \
adding up all the incidences of 0, 1, or 2 in the original list, \
then populating a new list starting from lowest number.
 
The second exercise, "Binary Search", has us 

"""


# Exercise "Sort an array of 0s, 1s, and 2s"

def sort_nums(unsorted_list):
    """
    This function counts the incidences of 0, 1, and 2 in a list input \
    and returns a list of those values sorted numerically
    """
    #incidence count for each number
    zeros = 0 
    ones = 0
    twos = 0
    sorted_list = [] #empty list for returning sorted values

    #loop to count incidences
    for i in unsorted_list: 
        if unsorted_list[i] == 0:
            zeros += 1
        if unsorted_list[i] == 1:
            ones += 1
        if unsorted_list[i] == 2:
            twos += 1
    
    #loops to append counted incidences to final list
    for i in range(zeros):
        sorted_list.append(0)
    for i in range(ones):
        sorted_list.append(1)
    for i in range(twos):
        sorted_list.append(2)
    
    #returns final, sorted list
    return sorted_list

#test list
unsorted_test = [0,2,1,0,0,1,2,0,2,0,1,2,1,0,2,1,0,1,2,0,1,2,0,1,0,2,0,1,2]

#stores result of test list
sorted_test = sort_nums(unsorted_test)

#prints sorted list for user
print(sorted_test)



# Exercise "Binary Search"