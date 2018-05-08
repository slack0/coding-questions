'''
Given an array of integers where each element points to the index of the next element 
how would you detect if there is a cycle in this array
Note: if the element of array is in range[0, n-1], where n is the length of array, then there must be at least one cycle.
Thus, the element may be negative or out of range[0,n-1]
'''

def detect_cycle(arr):
    visited = {}
    nxt = arr[0] ### start at the first element
    visited[nxt] = True
    while True:
        if nxt < 0 or nxt > len(arr):
            return False

        nxt = arr[nxt]
        print 'nxt index = {}'.format(nxt)
        if nxt in visited:
            return True
        else:
            visited[nxt] = True

if __name__=='__main__':
    import random
    n = random.randint(1,20)
    arr = [random.randint(0, n-1) for _ in range(n)]
    print 'array = {}'.format(arr)
    print 'array has cycle? {}'.format(detect_cycle(arr))

    arr = [-1, 1, 0, 2, 3]
    print 'array = {}'.format(arr)
    print 'array has cycle? {}'.format(detect_cycle(arr))


