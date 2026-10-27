class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        res=[]
        # store frequency of each number using hashmap
        for i,val in enumerate(nums):
            freq[val] = freq.get(val,0) + 1
        # init a array of subarray. Subarray indices represent the occurrence of the values in them i.e. if 1 in stored at freq[3] it means 1 occured 3 times.
        freq_array = [[] for i in range(len(nums)+1)]

# store the freq_map into the subarrays based on their occurence
        for key,val in freq.items():
            freq_array[val].append(key)
# Loop the freq_array in reverse because we have to pick the highest and when length of response gets equal to the k reutrn it.
        for i in range(len(freq_array)-1,0,-1):
            for j in freq_array[i]:
                res.append(j)
                if len(res)==k:
                    return res
