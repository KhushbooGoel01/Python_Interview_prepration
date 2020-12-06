Problem Statement

Implement the isSubset(int* arr1, int* arr2, int size1, int size2) function, which will take two arrays and their sizes as input and check whether one array is the subset of the other.

Note: The input arrays do not contain duplicate values.

Input 

Two arrays of integers and their sizes.

Output 
true if arr2 is a subset of arr1.



arr_one = [4,5,6,9,8]
arr_two = [4,5]

def is_subset(arr_one, arr_two):
    len_one = len(arr_one)
    len_two = len(arr_two)
    arr_one_hash = {}
    for value in arr_one:
        arr_one_hash[ value ] = 1
    
    print( arr_one, arr_two, arr_one_hash)
    
    
    '''for value in arr_two:
        if not arr_one_hash.get(value):
            return False'''
            
     #both ways work, it's just preference       
    
    if not all( arr_one_hash.get( value)  for value in arr_two  ): return False
    else: return True
    
print ( is_subset(arr_one, arr_two))
