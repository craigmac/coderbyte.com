#! /usr/bin/python

''' (num) -> str

Given num as representing minutes, returns a string displaying how many hours
and minutes it results in.

Example usage:
>>> TimeConvert(63)
1:3
>>> TimeConvert(37)
0:37
>>> TimeConvert(120)
2:00

'''

def TimeConvert(num):
    # Convert to int.
    t = int(num)
    end = '(hours:minutes)'
    
    # Test if 0 or less.
    if t <= 0:
        return '0:00' + end
    # Test if no minutes required
    elif t % 60 == 0:
        return str(t / 60) + ':00' + end
    else:
        mins = t % 60 # Remainder is the minutes
        return str(t / 60) + ':' + str(mins) + end

print TimeConvert(raw_input('Enter minutes to convert to hours: '))



