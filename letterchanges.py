#! /usr/bin/python

def LetterChanges(sen):

    '''(str)->str
        
    Take sen and replace every letter in the string with the letter
    following it in the alphabet (e.g., c becomes d, z becomes a). 
    Then capitalize every vowel in this new string (a,e,i,o,u).

    Ignores most non-alphabet characters such as !?@#$_-/, etc.

    >>> LetterChanges('change!')
    'dIbOhf!'
    >>> LetterChanges('abcde')
    'bcdEf'
    >>> LetterChanges('Zz!?abd')
    'zA!?bcE'
    '''

    # Split the sentence up into an array. 
    string = []
    for char in sen[:]:
        string.append(char)

    # Increment each, accounting for undesirables.
    for i in range(len(string)):
        if string[i] not in '<,.>?/\'\":;`~!@#$%^&*()-_+=|\\':
            if ord(string[i]) == 122:
                string[i] = 'a'
            elif ord(string[i]) == 90:
                string[i] = 'z'
            else:
                string[i] = chr(ord(string[i])+1)
    # Capitalize the vowels not already capitalized.
    for i in range(len(string)):
        if string[i] in 'aeiou':
            string[i] = string[i].capitalize()

    # Join array back into a sentence.
    return ''.join(string)

print(LetterChanges(input('Enter a sentence to change: ')))


      


