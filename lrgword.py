#! /usr/bin/python

def LongestWord(sen):

    '''(str) -> str

    Return the longest word in the string. If a tie, will list all
    tied words for longest. Remove the following variables:
    ',\"\'.;:?!@#$%^&*()-+_={}[]<>~`'
    
    >>> LongestWord('longest word will be the first!!!!!!')
    'longest'
    >>> LongestWord('short, words. match??')
    'It's a tie between':
    'short'
    'words'
    'match'
    '''
    
    stripchars = ',\"\'.;:?!@#$%^&*()-+_={}[]<>~`'

    for char in sen:
        if char in stripchars:
            sen = sen.replace(char,'')
    return sen


# Use raw_input because input() fed the sentence to LongestWord
# with quotes around it, causes error when you use apostrophe in
# the sentence without escaping it
# LongestWord(input('It's a wonderful life!')) causes error because it
# tries to create just the string 'It'
sentence = (LongestWord((raw_input('Enter a sentence/s: ') ))) 

# Split sentence into list
words = sentence.split()

biggest = ['']

# Find the biggest or if tied, add those as well
for word in words:
    if len(word) > len(biggest[0]):
        biggest[0] = word
    elif len(word) == len(biggest[0]):
            biggest.append(word)

# Print it all out
print('The longest string length is: ' + str(len(biggest[0])))
if len(biggest) == 1:
    print('The longest word is: ' + str(biggest[0]))
else:
    print('A tie for the longest word! They are: ')
    for i in biggest:
        print(i)


