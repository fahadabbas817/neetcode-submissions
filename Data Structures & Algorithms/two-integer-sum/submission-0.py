class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complement = 0
        seen = {}
        
        for i, val in enumerate(nums):

            complement = target - val

            if complement in seen:
                 return [seen[complement],i]
            
            seen[val] = i
               

