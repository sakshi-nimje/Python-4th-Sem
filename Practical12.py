'''Write a program to print next 5 days starting from today'''

import datetime

# Get today's date
today = datetime.date.today()

# Print the next 5 days
for i in range(1, 6):
    next_day = today + datetime.timedelta(days=i)
    print(next_day.strftime('%A, %B %d, %Y'))
    
'''
Output:
Saturday, May 06, 2023
Sunday, May 07, 2023
Monday, May 08, 2023
Tuesday, May 09, 2023
Wednesday, May 10, 2023
'''   
