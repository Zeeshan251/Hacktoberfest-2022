'''
Name:- JANUMALA AKHILENDRA
LANGUAGE:-PYTHON
JUMP SEARCH
'''

import math

def jump_search(A, item):
    print("Entering Jump Search")
    n = len(A)                          # Length of the array
    m = int(math.sqrt(n))               # Step length
    i = 0                               # Starting interval

    while i != len(A)-1 and A[i] < item:
        print("Processing Block - {}".format(A[i: i+m]))
        if A[i+m-1] == item:            # Found the search key
            return i+m-1
        elif A[i+m-1] > item:           # Linear search for key in block
            B = A[i: i+m-1]
            return linear_search(B, item, i)
        i += m

    B = A[i:i+m]                        # Step 5
    print("Processing Block - {}".format(B))
    return linear_search(B, item, i)


def linear_search(B, item, loc):
    print("\t Entering Linear Search")
    i = 0

    while i != len(B):
        if B[i] == item:
            return loc+i
        i += 1
    return -1    