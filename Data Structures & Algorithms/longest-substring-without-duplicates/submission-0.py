class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = {}
        i=0
        maxLen=0
        for j,val in enumerate(s):
            
            if val in unique and unique[val]>=i:
                i = unique[val] + 1


            unique[val] = j
            maxLen = max(maxLen,j-i+1)

        return maxLen