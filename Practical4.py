'''Write a python program using function to check who is employee month.'''

'''The employee of the month is the one with the highest number of hours worked in the month.'''

def get_employee_of_the_month(employees):
    employee_of_the_month=""
    max_hours = 0

    for employee, hours in employees.items():
        if hours > max_hours:
           max_hours= hours

           employee_of_the_month = employee
    return employee_of_the_month

employees = {"Sunil": 160, "Amit": 200, "Sanjay": 180, "Rahul": 190, "Rohan": 195}

employee_of_the_month = get_employee_of_the_month(employees)
print(f"The employee of the month is {employee_of_the_month}.")


'''
Output:
The employee of the month is Amit.
'''