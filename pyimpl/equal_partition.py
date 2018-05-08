'''
Given an array with integers,  find the index to minimize the difference between 
left part sum and right part sum, not including the index number itself, return the position of the integer.  
'''

'''

solution: Calculate the sum of array. Scan the array, maintain a left sum and right sum, and record the minimal difference.
O(n) time, O(1) space

'''

import sys
def equal_halves(arr):
    total = sum(arr)
    mindiff = sys.maxint
    min_idx = None
    for i, e in enumerate(arr):
        left_sum = sum(arr[:i])
        right_sum = total - left_sum - e
        if abs(left_sum - right_sum) < mindiff:
            mindiff = abs(left_sum - right_sum)
            min_idx = i

    return min_idx

if __name__=='__main__':
    arr = [1, 5, 7, 12, 10, 11, 7, 5, 1]
    print 'array = {}'.format(arr)
    print 'partition = {}'.format(equal_halves(arr))


