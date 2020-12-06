Problem Statement 

You have to implement the bool isDisjoint(int* arr1, int* arr2, int size1, int size2) function, which checks whether two given arrays are disjoint or not.

Two arrays are disjoint if there are no common elements between them. The assumption is that there are no duplicate elements in each array.

Input 

Two arrays of integers and their lengths.

Output 

It returns true if the two arrays are disjoint. Otherwise, it returns false.


arr_one = [4,5,6,9,8]
arr_two = [0,3]

def is_subset(arr_one, arr_two):
    len_one = len(arr_one)
    len_two = len(arr_two)
    arr_one_hash = {}
    for value in arr_one:
        arr_one_hash[ value ] = 1
    
    #print( arr_one, arr_two, arr_one_hash)
    
    
    '''for value in arr_two:
        if not arr_one_hash.get(value):
            return True'''
            
    
    if not any( arr_one_hash.get( value)  for value in arr_two  ): return True
    else: return False
    
print ( is_subset(arr_one, arr_two))

