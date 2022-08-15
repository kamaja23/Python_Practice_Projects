'''###Given a 2D Array,

:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

An hourglass in
is a subset of values with indices falling in this pattern in

's graphical representation:

a b c
  d
e f g

There are
hourglasses in . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be

.

Example

-9 -9 -9  1 1 1
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0

The

hourglass sums are:

-63, -34, -9, 12,
-10,   0, 28, 23,
-27, -11, -2, 10,
  9,  17, 25, 18

The highest hourglass sum is
from the hourglass beginning at row , column

:

0 4 3
  1
8 6 6

Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

Function Description

Complete the function hourglassSum in the editor below.

hourglassSum has the following parameter(s):

    int arr[6][6]: an array of integers

Returns

    int: the maximum hourglass sum

Input Format

Each of the
lines of inputs contains space-separated integers

.

Constraints

Output Format

Print the largest (maximum) hourglass sum found in

.

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output

19

Explanation

contains the following hourglasses:

image

The hourglass with the maximum sum (

) is:

2 4 4
  2
1 2 4
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
#My contribution to the code
def hourglassSum(arr):
    res = []
    for ix,x in enumerate(arr):
        for iy,y in enumerate(x):
            a = []
            try:
                for h in range(1,4):
                    a.append(arr[ix][iy+h-1])
                    a.append(arr[ix+2][iy+h-1])
                    if h == 2 :
                        a.append(arr[ix+1][iy+h-1])
            except:
                break
            res.append(a)
    return(max([sum(i) for i in res]))
#End of my contribution
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
