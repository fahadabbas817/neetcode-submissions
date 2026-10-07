class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        i = 0
        freq = {}
        highFreq=0

        for j,val in enumerate(s):
            # evaluate frequencie of all values in a string
            freq[val] = freq.get(val,0) + 1
            # evaluate highest frequency in particular iteration
            highFreq = max(highFreq,freq[val])

            curr_len = j-i+1
            # expand the window if valid Note:Use while loop is standard for shriking but its optimization for this specific problem where there is only one step either side.
            if curr_len - highFreq <= k:
                maxLen = max(maxLen,curr_len)
            # Shrink the window from left and decrease frequency of that char
            else:
                freq[s[i]] -= 1
                i+=1
        
        return maxLen
