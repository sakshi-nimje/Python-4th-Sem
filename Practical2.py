'''Print every word from the below sentence which has an even number of letters-St-"print only the word that starts with s in this sentence".'''

str="print only the words that starts with s in this sentence"

s=str.split(" ")

for i in s:
    if len(i)%2==0:
        print(i)


'''
Output:
only
that
starts
with
in
this
sentence
'''    

