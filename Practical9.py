'''Write a python function to multiply all the numbers in the list'''

def multiply_numbers(my_List):
    result = 1
    for x in my_List:
        result = result * x
    return result
 
list = [1, 2, 3, 4, 5]
print(multiply_numbers(list))

'''
Output:
120
'''