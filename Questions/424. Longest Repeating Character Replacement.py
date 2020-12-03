Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
 

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.


from collections import Counter
def Max_string(s,k):
    s= list(s)
    pt1=0
    pt2=0
    d = Counter(s)
    for i in range(len(s)):
        




      
  Q2. Variation of https://leetcode.com/problems/longest-repeating-character-replacement/
Given an array consists of integers (ex. [1,2,3,1,2,3,3,3]), the required returning value is the length of longest substring that consists of repeating integer value you can get with maximum 3 replacements (and you can replace any item with any value).
Test cases:

Input: A = [1,2,3,1,2,3,3,3]
Output: 6
Replace A[1], A[3], A[4] with 3 (3 moves)

Input: A = [1,2,7,8,3,45]
Output: 4
Pick any item and replace 3 items adjacent to that item with the value of the picked item.


import collections
def maxSub(nums):
    myC = collections.Counter()
    maxf = p1 = p2 = 0

    while p2 < len(nums):
        myC[nums[p2]] += 1
        maxf = max(maxf, myC[nums[p2]])

        if p2 - p1 + 1 > maxf + 3:
            myC[nums[p1]] -= 1
            p1 += 1
        p2 += 1
    return len(nums) - p1

A=[[3,1,3,2,5,3],[3,1,3,2,5,1,9,7],[0,0,1,1,1,0],[2,1,2,2,3],[1,1,2,2,2,2,2,3,5] ]


for nums in A:
    print('nums is',nums,'max sub is',maxSub(nums))
  
  
  https://leetcode.com/discuss/interview-question/927457/Google-or-OA-or-2021-SWE-Internship

