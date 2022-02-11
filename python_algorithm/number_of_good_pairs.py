#1512. Number of Good Pairs
"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

# Time complexity (n*2)
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        
        res = 0
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                
                if nums[i] == nums[j] and i < j:
                    res+=1
                else:
                    pass
        return res
    
    """ 
    timecomplexity (N)
    class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashMap = {}
        res = 0
        for number in nums:            
            if number in hashMap:
                res += hashMap[number] # 1이 이미 들어가 있으므로 1을 올리고 앞에 있는 1도 올려준다. 
                hashMap[number] += 1
            else:
                hashMap[number] = 1
        return res
    """