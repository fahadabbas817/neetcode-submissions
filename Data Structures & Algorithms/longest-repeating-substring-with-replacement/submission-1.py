class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        i = 0
        freq = {}

        for j,val in enumerate(s):

            if val not in freq:
                freq[val] = 1
            else:
                freq[val] += 1
            
            highest = max(freq.values())
            curr_len = j-i+1

            if curr_len - highest <= k:
                maxLen = max(maxLen,curr_len)
            else:
                freq[s[i]] -= 1
                i+=1
        
        return maxLen
