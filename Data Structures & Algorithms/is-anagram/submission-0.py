class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_s = {}
        for i, val in enumerate(s):
            char_s[val] = char_s.get(val,0) + 1
        print(char_s)
        char_t = {}
        for i, val in enumerate(t):
            char_t[val] = char_t.get(val,0) + 1
        
        return char_s == char_t
            

            
        