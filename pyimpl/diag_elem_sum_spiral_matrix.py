'''

Diagonal elements sum of spiral matrix
For example: 
Input:
25 24 23 22 21 
10 9  8  7 20 
11 2  1  6 19 
12 3  4  5 18 
13 14 15 16 17 
Output: 
45 (21 + 7 + 1 + 3 + 13) 

'''

def diag_sum(M):
    nrows = len(M)
    ncols = len(M[0])

    dsum = 0
    for i in range(nrows):
        dsum += M[i][ncols-i-1]

    return dsum


if __name__=='__main__':
    M = [[25,24,23,22,21],
    [10,9,8,7,20],
    [11,2,1,6,19],
    [12,3,4,5,18],
    [13,14,15,16,17]]

    print '{}'.format(M)
    print 'sum of diag elements = {}'.format(diag_sum(M))
