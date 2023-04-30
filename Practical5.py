''' Write a program to mimic the carnival game 'Three Cup Montee'. '''

import random  #we need a module shuffle a list to mix
mylist = ['', 'R', '']      #we create our list according to 3 possibilities
random.shuffle(mylist)
print(mylist)

def shuffle_list(mylist):
    random.shuffle(mylist)
    return mylist
shuffle_list(mylist)

def player_guess():
    guess = ''          #We start with an empty guess
    while guess not in ['0','1','2']:
        guess = input("Pick a number : 0 , 1 or 2\n")
    return int(guess)

def check_guess(mylist , guess):
    if mylist[guess] == 'R':
        print("Correct ! You Won")
    else:
        print("Wrong guess! Please try again")
        print(mylist)
        
#Initial list
mylist = ['', 'R' , '']

#Shuffle List (function-1)
mixedup_list = shuffle_list(mylist)

#User guess (function-2)
guess = player_guess()

#Check guess (function-3)
check_guess(mixedup_list , guess)

'''
Output:

['', '', 'R']
Pick a number : 0 , 1 or 2
0
Wrong guess! Please try again
['', '', 'R']
**********************************************
['', '', 'R']
Pick a number : 0 , 1 or 2
1
Wrong guess! Please try again
['R', '', '']
**********************************************
['R', '', '']
Pick a number : 0 , 1 or 2
2
Wrong guess! Please try again
['', 'R', '']
**********************************************
['R', '', '']
Pick a number : 0 , 1 or 2
1
Correct ! You Won'''
