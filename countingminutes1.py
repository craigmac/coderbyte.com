#! /usr/bin/python
import datetime as dt
import time

'''
Using the Python language, have the function CountingMinutesI(str) take the str
parameter being passed which will be two times (each properly formatted with a
colon and am or pm) separated by a hyphen and return the total number of minutes
between the two times. The time will be in a 12 hour clock format.

For example:
if str is 9:00am-10:00am then the output should be 60. If str is 1:00pm-11:00am
the output should be 1320.
'''

def CountingMinutesI(string):

    # Place individual times in a list.
    times = string.split('-')

    # time.strptime() makes time object from str, then time object is turned back
    # to str using time.strftime()
    start = time.strftime("%H:%M", time.strptime(times[0], "%I:%M%p"))
    print start
    end = time.strftime("%H:%M", time.strptime(times[1], "%I:%M%p"))
    print end

    # Turn them into datetime objects to do comparison.
    # So from the beginning we go:
    # str -> time object -> str -> datetime ojbect
    # e.g., if 9:00am were given -> 1900-01-01 09:00:00
    start_dt = dt.datetime.strptime(start, '%H:%M')
    end_dt = dt.datetime.strptime(end, '%H:%M')
    
    diff = (end_dt - start_dt) # e.g. 1:00:00 for one hour difference
    return (diff.seconds/60)
    # We can say diff.seconds because diff is still a datetime object. 
    
    
    
    
print CountingMinutesI('9:00am-10:00am') # -> 60

