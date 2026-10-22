class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0
        for n in numsSet:
            seq = 0 
            if n-1 not in numsSet:
                x = n
                seq += 1
                while x+1 in numsSet:
                    seq += 1
                    x += 1
                res = max(res, seq)
        
        return res