'''
Find the rotation distance of a rotated sorted array. 
For example:
input:
4, 5, 6, 1, 2, 3
output:
3
input:
1, 2, 3, 4, 5, 6
output:
0
input:
2, 3, 4, 5, 6, 1
output:
1
'''

def rotation_dist(arr):
    curr_min = new_min = arr[0]
    for i, e in enumerate(arr[1:]):
        new_min = min(e, new_min)
        if new_min != curr_min:
            return len(arr) - i - 1
    return 0

if __name__=='__main__':
    import random
    n = random.randint(3,10)
    rot = random.randint(0, n-1)

    a1 = list(range(n)) ### create an array
    a1 = a1[rot:] + a1[:rot] ### shift around by 'rot'

    rot_dist = rotation_dist(a1) ### calculate rot_dist
    print 'arr = {} rotation = {}\tcalculated rotation = {}'.format(a1, rot, rot_dist)
    assert rot_dist == rot ### check if they are the same

    # a2 = [4, 5, 6, 1, 2, 3]
    a2 = [1, 2, 3, 4, 5, 6]
    print '{} rotation = {}'.format(a2, rotation_dist(a2))

    a3 = [1, 2, 3, 4, 5, 6, 0, -1]
    print '{} rotation = {}'.format(a3, rotation_dist(a3))


