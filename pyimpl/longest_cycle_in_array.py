'''
Given an array of integers where each element points to the index of the next element 
how would you detect the longest cycle in this array.
Note: suppose the element of array is in range[0, n-1], where n is the length of array, then there 
must be at least one cycle. If one element points itself, this particular cycle length is 1.
'''

def longest_cycle(arr):
    current = []
    longest = []

    for e in arr:
        current = get_cycle(arr, e)
        if len(current) > len(longest):
            longest = current[:]

    return longest

def get_cycle(arr, e):
    visited = {}
    cycle = [e]
    nxt = arr[e] ### start at the first element
    visited[nxt] = True
    cycle.append(nxt)

    while True:
        if nxt < 0 or nxt > len(arr):
            return None

        nxt = arr[nxt]
        print 'nxt index = {}'.format(nxt)
        cycle.append(nxt)
        if nxt in visited:
            return cycle
        else:
            visited[nxt] = True

if __name__=='__main__':
    import random
    n = random.randint(1,20)
    arr = [random.randint(0, n-1) for _ in range(n)]
    print 'array = {}'.format(arr)
    print 'longest cycle = {}'.format(longest_cycle(arr))

