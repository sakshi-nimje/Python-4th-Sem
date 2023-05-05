'''Write a python function to that accepts a string and calculate the number of upper case letters and lower case letters'''

def count(string):
    
    upper= 0
    lower= 0

    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    return (upper, lower)

string = input("Enter the string :")
upper,lower = count(string)

print("The number of upper case letters is: ", upper)
print("The number of lower case letters is: ", lower)

'''
Output:
Enter the string :PYTHON is a popular programming language
The number of upper case letters is:  6 
The number of lower case letters is:  29
'''
