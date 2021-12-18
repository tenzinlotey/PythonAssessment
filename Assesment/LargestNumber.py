"""
Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers. 
Note: Assume that all the numbers are two digit numbers.

"""

def create_largest_number(number_list):
    #remove pass and write your logic here
    largest_number = ""
    number_list.sort(reverse = True )
    for num in number_list:
        largest_number += str(num)
    return int(largest_number)
        

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)