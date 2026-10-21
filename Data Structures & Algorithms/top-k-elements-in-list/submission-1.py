class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if nums is None or k is None or not nums or not k:
            return []
            
        # sol 1
        # count using hashmap
        # sort based on the freq
        # loop and get k elements 
        # Time: O(NlogN)
        # Space: O(N)
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        freq = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)

        res = []
        for i in range(k):
            res.append(freq[i][0])
        return res
        