'''Print only the words that start with letter 's in the following statement -St- 'print only the word that starts with s in this sentence.'''

string = 'print only the word that starts with s in this sentence'

for word in string.split():
  if word[0] == 's':
      print(word)
      
      
'''
Output:
starts
s       
sentence
'''