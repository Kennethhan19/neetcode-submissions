class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums is None or not nums:
            return []

        # two arrays for tracking post and pre
        # time: O(N)
        # space: O(N)

        pre_prod = [1 for i in range(len(nums))]
        for i in range(1, len(nums), 1):
            pre_prod[i] = nums[i-1]*pre_prod[i-1]

        post_prod = [1 for i in range(len(nums))]
        for i in range(len(nums)-2, -1, -1):
            post_prod[i] = nums[i+1]*post_prod[i+1]

        res = []
        for i in range(len(nums)):
            res.append(pre_prod[i]*post_prod[i])

        return res