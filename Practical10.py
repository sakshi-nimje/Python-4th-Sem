'''Write a program for validating the user input'''
        
        
while True:
    user_input = int(input("Enter a positive integer between 1 and 10: "))
    try:
        if user_input < 1 or user_input > 10:
            print("Input must be between 1 and 10. Please try again.")
        else:
            print("Input is valid!")
            break
    except ValueError:
        print("Input must be a positive integer. Please try again.")

'''
Output:
Enter a positive integer between 1 and 10: 88
Input must be between 1 and 10. Please try again.
Enter a positive integer between 1 and 10: 3     
Input is valid!
'''       
        
        
        