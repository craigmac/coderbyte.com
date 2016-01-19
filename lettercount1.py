#! /usr/bin/python

'''Using the Python language, have the function LetterCountI(str) take the
str parameter being passed and return the first word with the greatest number
of repeated letters. For example: "Today, is the greatest day ever!" should
return greatest because it has 2 e's (and 2 t's) and it comes before ever
which also has 2 e's. If there are no words with repeating letters return -1.
Words will be separated by spaces. '''

def LetterCountI(string):
    '''(str) -> str'''

    split_words = string.split()
    counts = {}

    # Create a dictionary for each entry
    for word in split_words:
        counts[word] = 0

    # Loop each entry, going character by character and doing a count of
    # that character within the word.
    for word in split_words:
        for char in word:
            if word.count(char) > counts[word]: # Check if letter occurence biggest.
                counts[word] = word.count(char)

    print '\nHere are the words with their max character repeat values: '
    print counts

    # Get the values from the dict.
    # Had to remove the extra square brackets from around 'counts.values()'
    # because .values() returns a list, so it was double bracketed
    # e.g. [[3, 1, 2, 1, 1]] instead of just [3, 1, 2, 1, 1]
    # It caused the max() method not to work, unless we had said max(val[0]).
    
    val = counts.values() 

    # Find the largest value.
    lrgval = max(val)

    # Create a new dict to hold key/value pairs that match largest value.
    results = {}
    
    # First unpack the list, e.g. [('one', 3), ('two', 1)] that .items() returns.
    # When a list contains parenthesis, e.g. [('one', 2)] python can assign a variable
    # to both 'one' and 2 in this case. Without parenthesis, e.g. ['one', 2, 'two', 3]
    # each entry is considered a separate entry, thus saying 'for x,y in ...' would
    # then give an error. 
    for k, v in counts.items(): # Returns a list of tuples (key and values of dict).
        if v == lrgval:
            results[k] = v

    # If only one winner, print it.
    if len(results) == 1:
        print '\nThe word with the longest repeating character was: \n'
        for x in results:
            print 'Word: ' + x
            print 'Repeating Letters: ' + str(results.get(x))

    # More than one word with same number of repeat letters.
    else:
        print '\nThere was a tie between words: '
        for x in results:
            print 'Word: ' + x
            print 'Repeating Letters: ' + str(results.get(x)) + '\n'

##LetterCountI('fiiirst second third fourth fiffth') # Longest should be fifth
print 'Enter a sentence below. The program will find which word',
print 'contains the most amount of repeated characters.'
print 'For instance, \'alabama\' has 3 a\'s.'
print '\nCTRL-C to quit at any time.'
LetterCountI(raw_input('> '))
