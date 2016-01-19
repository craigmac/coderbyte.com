#! /usr/bin/python

'''(str) -> str

Return (str) in reverse order.

Example usage:
>>> AlphabetSoup(string)
gnirts
>> AlphabetSoup(hello!)
!olleh

'''

def AlphabetSoup(str):
    return str[::-1] # [from:to:step]

print AlphabetSoup(raw_input('Enter a string to reverse: '))
