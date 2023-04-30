'''Write a program that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.'''

def lesser_of_two_evens(a,b):
    if (a%2==0 and b%2==0):
        print(min(a,b))
    else:
        print(max(a,b))
        
x = int(input("Enter x : "))
y = int(input("Enter y : "))

lesser_of_two_evens(x,y)

'''
Output:
Enter x : 2
Enter y : 4
2

Enter x : 3
Enter y : 4
4

Enter x : 7
Enter y : 2
7
'''