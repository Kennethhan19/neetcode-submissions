class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(N)
        return len(nums) != len(set(nums))
        