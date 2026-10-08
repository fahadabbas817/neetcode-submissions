class Solution:
    def minWindow(self, s: str, t: str) -> str:
      
        if t == "":
            return ""

        countT, window = {}, {}

        # 1. Populate the frequency map for the target string
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('inf')
        i = 0

        # 2. Slide the right pointer across the string
        for j in range(len(s)):
            c = s[j]
            window[c] = window.get(c, 0) + 1

            # If the current character satisfies the exact frequency needed
            if c in countT and window[c] == countT[c]:
                have += 1

            # 3. Shrink the window from the left while it remains valid
            while have == need:
                # Update our result if this is the smallest valid window so far
                if (j - i + 1) < resLen:
                    res = [i, j]
                    resLen = j - i + 1
                
                # Remove the left character from our window
                window[s[i]] -= 1
                
                # If removing it breaks our "need" condition, update `have`
                if s[i] in countT and window[s[i]] < countT[s[i]]:
                    have -= 1
                    
                i += 1
                
        # 4. Return the result (Out of the loop!)
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""