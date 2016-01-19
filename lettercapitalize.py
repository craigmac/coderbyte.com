#! /usr/bin/python

def LetterCapitalize(str):

    '''(str) -> str

    Capitalize the first letter of each word found in str.

    >>> LetterCapitalize('I am the best!')
    'I Am The Best'
    >>> LetterCapitalize('good-golly miss molly?')
    'Good-golly miss molly?'
    '''
    words = str.split()
    # Can't use 'for word in words:' loop because we need to
    # explicitly state what index num, e.g., words[w],
    # words[word] won't work because word is a str
    for w in range(len(words)):
        capword = words[w].capitalize()
        words[w] = capword
        w += 1

    return ' '.join(words)

print(LetterCapitalize('good-golly miss molly'))
