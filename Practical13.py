'''Write a function that asks for an integer and prints square of it. Use a while loop with try, except, else block account for incorrect inputs.'''

def print_square():
    while True:
        try:
            num = int(input("Enter an integer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
        else:
            print(f"The square of {num} is :", num**2)
            break
        
print_square()

'''
Output:
Enter an integer: 6.9
Invalid input. Please enter an integer.
Enter an integer: 4
The square of 4 is : 16
'''
