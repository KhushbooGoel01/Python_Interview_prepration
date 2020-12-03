Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].


def wigglesort(l):
    l=sorted(l)
    for i in range(1,len(l),2):
        l.insert(i,l[-1])
        l.pop()
    return l
    
    
def wigglesor(l):
for i in range(len(l)):
    if (i % 2 == 0) == (nums[i] > nums[i + 1]): 
        sawp(l, i, i+1)
return l
        
