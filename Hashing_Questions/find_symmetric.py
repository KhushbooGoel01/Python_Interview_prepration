Problem Statement 

By definition, (a, b) and (c, d) are symmetric pairs if, a = d and b = c. In this problem, you have to implement the string findSymmetric(int arr[][2], int size) function, which will find all the symmetric pairs in the given array.

Input 

A 2-D Array and the number of rows in the array.

Note: The first value in the pair should be unique.

Output 

A string containing all the symmetric pairs of integers in the input array.


input = 4 5 
5 4
2 2
1 2
6 3 
3 6


code:::
n= 6
pair_list = []

for y in range(n):
    pair_list.append(( input().split()))
    
def find_symmetric( pair_list ):
    pair_hash= {}
    for (a,b) in pair_list:
        pair_hash[ (a,b) ] = 1
    ans_list =[]
    
    #print( pair_list, pair_hash)
    
    for (a,b) in pair_list:
        
        (a,b) = (b,a)
        
        if a==b:
            continue
        #print(pair_hash.get((a,b)))
        if pair_hash.get((a,b)):
            #print(pair_hash.get((a,b)))
            ans_list.append((a,b))
            
    return ans_list
    
print( *find_symmetric(pair_list) )
    
