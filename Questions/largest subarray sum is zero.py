Find the length of largest subarray with 0 sum
Given an array of integers, find length of the largest subarray with sum equals to 0.

Examples :

Input: arr[] = {15, -2, 2, -8, 1, 7, 10, 23};
Output: 5
The largest subarray with 0 sum is -2, 2, -8, 1, 7


def max_len(arr):
    ans=0
    for i in range(len(arr)):
        carry_sum=0
        for j in range( i, len(arr)):
            carry_sum += arr[j]
            ans =  max(ans, j-i+1)
    return ans

def maxx(arr):
    hash_map = {} 
    max_len = 0
    curr_sum = 0
    for i in range(len(arr)): 
        curr_sum += arr[i] 
        if arr[i] ==0 and max_len ==0: 
            max_len = 1
        if curr_sum == 0: 
            max_len = i+1
        if curr_sum in hash_map: 
            max_len = max(max_len, i - hash_map[curr_sum] ) 
        else: 
            hash_map[curr_sum] = i 
  
    return max_len 
  
arr = [15, -2, 2, -8, 1, 7, 10, 13] 
   
print ("Length of the longest 0 sum subarray is %d" %  maxx(arr) )


