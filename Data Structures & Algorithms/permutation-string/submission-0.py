class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is larger than s2, a permutation is impossible
        if len(s1) > len(s2):
            return False
            
        # Frequency arrays for 26 lowercase letters
        count1 = [0] * 26
        count2 = [0] * 26
        
        # 1. Setup the initial window
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
            
        # 2. Slide the window exactly 1 character at a time
        for i in range(len(s1), len(s2)):
            # If the frequency arrays match, we found a permutation
            if count1 == count2:
                return True
                
            # Add the new character on the right of the window
            count2[ord(s2[i]) - ord('a')] += 1
            
            # Remove the old character that fell out the left of the window
            left_char_index = i - len(s1)
            count2[ord(s2[left_char_index]) - ord('a')] -= 1
            
        # 3. Check the very last window after the loop ends
        return count1 == count2