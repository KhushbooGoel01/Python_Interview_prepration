https://leetcode.com/discuss/interview-question/396769/

You are given a string that represents time in the format hh:mm. Some of the digits are blank (represented by ?). Fill in ? such that the time represented by this string is the maximum possible. Maximum time: 23:59, minimum time: 00:00. You can assume that input string is always valid.

Example 1:

Input: "?4:5?"
Output: "14:59"
Example 2:

Input: "23:5?"
Output: "23:59"

def max_time(s):
  s = list(s)
  if s[0] =='?':
    if s[1]>4: s[0]=1
    else: s[0] = 2
  if s[1] =='?':
    if s[0] ==2: s[1] = 3
    else: s[1] = 9
  if s[3] == '?': s[3] = 5
  if s[4] == '?': s[4] = 9
  return "".join(s)
  
  
  Q1. Variation of https://leetcode.com/discuss/interview-question/396769/
Problem setting was same with the link above, but the required output was the number of valid times given the input such as "??:??".
Test cases:

Input: "??:??"
Output: 1440

Input: "0?:14"
Output: 10


def valid_time_count(s)
  s= list(s)
  ans=1
  if s[4] =='?': ans*10
  if s[3] =="?": ans*6
  if s[1]=="?" and s[0] =="?": ans*24
  if s[1]=="?" and s[0] =="2": ans*4
  if s[1]=="?" and s[0] =="1": ans*10
  if s[1]=="?" and s[0] =="0": ans*10
  if s[0]=="?" and int(s[1]) >4: ans*2
  
  return ans
  
  
  
  
  
  


