You are a traveling salesperson who travels back and forth between two cities (A and B).
You are given a pair of arrays (revA and revB) of length n.
You can only sell goods in one city per day.
At the end of each day you can choose to travel to another city but it will cost a constant amount of money (travelCost).
Example::
A = [3, 7,2,100]
B = [1,1,1,10]
n = 4
c = 2
MaximumProfile: 112

def maxprofit( revA, revB, c ):
    maxA = A[ n-1 ]
    maxB = B[ n-1 ]
    for i in range(-1, -1, -1):
        tempA = max( A[i] + maxA, A[i] + maxB - c )
        tempB = max( B[i] + maxB, B[i] + maxA - c )
        maxA = tempA
        maxB = tempB
        
    return max( maxA, maxB)
