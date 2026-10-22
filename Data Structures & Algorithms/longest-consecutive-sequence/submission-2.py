class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find beginning of sequence 
        # loop from there (keep checking n+1)
        # time: O(N) -- at most we loop thru list twice so 2(N)
        # space: O(N)
        numsSet = set(nums)
        res = 0
        for n in numsSet:
            if n-1 not in numsSet:
                seq = 1
                while n+seq in numsSet:
                    seq += 1
                res = max(res, seq)
        
        return res