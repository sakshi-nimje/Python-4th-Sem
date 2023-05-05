'''Write a python function that takes a list and returns a new list with the unique elements of the first lists.
For example: Sample list = [1, 1, 1, 2, 2, 3, 3, 4] , Unique list = [ 1, 2, 3, 4]'''

def unique_list(list):
    x = []
    for a in list:
        if a not in x:
            x.append(a)
    return x

print(unique_list([1, 1, 1, 2, 2, 3, 3, 4])) 

'''
Output:
[1, 2, 3, 4]
'''
