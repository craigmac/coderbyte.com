#! /usr/bin/python

'''
Using the Python language, have the function DashInsert(num) insert dashes
('-') between each two odd numbers in num. For example: if num is 454793
the output should be 4547-9-3. Don't count zero as an odd number.
'''

def DashInsert(num):
    '''(num) -> str '''
    
    nums = str(num)
    num_list = []
    ans_list = []
    
    # Get all numbers into a list.
    for n in nums:
        num_list.append(n)


    # Append to ans_list as needed.
    for i in range(len(num_list)):
        if i == len(num_list)- 1: # Last number in list.
            ans_list.append(num_list[i])
            return "".join(ans_list)
        elif int(num_list[i]) % 2 == 0: # Even case.
            ans_list.append(num_list[i])
        else: # Odd case.
            if int(num_list[i + 1]) % 2 == 0: # Odd-Even combo.
                ans_list.append(num_list[i]) # Add the odd.
            else: # Odd-Odd case.
                ans_list.append(num_list[i])
                ans_list.append('-')
    return ''.join(ans_list)


print DashInsert(454793)
print DashInsert(45479312237)
print DashInsert(557793)
