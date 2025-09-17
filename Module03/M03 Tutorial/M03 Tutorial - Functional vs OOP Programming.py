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
 
The second exercise, "Binary Search", has us find the index value for \
a number in a sorted list.  This is accomplised by finding the midpoint \
of the inputted list's length, then determining if the list value is equal to, \
less than, or greater than the search value.  If not equal, either the \
half of the list above or below is then searched for a midpoint and compared \
iteratively until the value matches or the list is fully searched.

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
print(f"Your sorted list is {sorted_test}.")



# Exercise "Binary Search"

def binary_search(unsearched_list, search_for): # creates search function with list to search and value to search for
    """
    This function accepts an organized list and a value, and searches \
    for the value in that list using binary search technique.
    """

    low = 0 # lowest index value of list to search, initially 0
    high = len(unsearched_list) - 1 # highest index value of list to search, initially set to the list length - 1, the last value in the list
    
    while low <= high: # loop to set mid value, check mid value against the search value, and adjust list search 
        mid = low + (high - low) // 2 # finds the integer value of the midpoint of list index
        
        if unsearched_list[mid] == search_for: #checks to see if the mid value is the search value
            return mid

        elif unsearched_list[mid] < search_for: # if midpoint is less than search value, moves the lower part of the search to be mid + 1
            low = mid + 1
        
        else: # if midpoint is greater than search value, moves the upper part of the search to be mid - 1
            high = mid - 1
    
    return -1 # returns -1 value if the search value is not found in the list 

#testing the bindary search function
test_list = [-50, -10, 0, 1, 4, 5, 7, 11, 22, 42, 442, 777, 4042]
test_value = 777

# stores the result of the bindary search for the test value within the test list
searh_result = binary_search(test_list, test_value)

print(f"The index value for {test_value} is {searh_result}.")