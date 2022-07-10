import math
import os
import random
import re
import sys
# Complete the 'biggerIsGreater' function below.
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
def biggerIsGreater(w):
    # Write your code here
    w =list(w)
    l1 = len(w) - 1
    while(l1 > 0 and w[l1-1] >= w[l1]):
        l1 -= 1
    if(l1 <= 0):
        return 'no answer'
    l2 = len(w) - 1
    while(w[l2] <= w[l1-1]):
        l2 -= 1
    w[l1-1], w[l2] = w[l2], w[l1-1]
    w[l1:] = w[len(w)-1:l1-1:-1]
    return ''.join(w)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    T = int(input().strip())
    for T_itr in range(T):
        w = input()
        result = biggerIsGreater(w)
        fptr.write(result + '\n')
    fptr.close()