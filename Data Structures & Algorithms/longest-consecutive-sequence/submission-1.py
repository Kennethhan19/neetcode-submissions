class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0
        for n in numsSet:
            if n-1 not in numsSet:
                seq = 1
                while n+seq in numsSet:
                    seq += 1
                res = max(res, seq)
        
        return res