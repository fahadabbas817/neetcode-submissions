class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = "".join(c.lower() for c in s if c.isalnum())

        left, right = 0, len(lower_s) - 1

        while left<right:

            if lower_s[left] != lower_s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True