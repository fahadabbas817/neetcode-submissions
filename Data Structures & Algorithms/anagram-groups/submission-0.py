
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        result = {}
        

        for string in strs:

            char_map = [0] * 26

            for char in string:

                char_map[ord(char)-ord('a')] += 1
            
            key = tuple(char_map)
            if key not in result:
                result[key]=[]
            result[key].append(string)
            
        return list(result.values()) 