class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums is None or not nums:
            return []

        # Sol 1
        # time: O(N^2)
        # space: O(1)
        # res = [0]*len(nums)
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         prod = prod*nums[j]
        #     res[i] = prod
        
        # return res

        # Sol 2
        # two arrays for tracking post and pre
        # time: O(N)
        # space: O(N)

        # pre[i] contains the product of the previous nums but not it self
        # which is why we need to compute nums[i-1]*pre[i-1]
        # because pre[i-1] does not include nums[i-1] 
        # same idea for post
        # pre = [1 for i in range(len(nums))]
        # for i in range(1, len(nums), 1):
        #     pre[i] = nums[i-1]*pre[i-1]

        # post = [1 for i in range(len(nums))]
        # for i in range(len(nums)-2, -1, -1):
        #     post[i] = nums[i+1]*post[i+1]

        # res = []
        # for i in range(len(nums)):
        #     res.append(pre[i]*post[i])
        # return res

        # sol 3
        # same idea but instead of extra array we use temp variable to hold cur product
        # time: O(N)
        # space: O(N)
        res = [1]*len(nums)

        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]

        post = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] *= post
            post *= nums[j]

        return res 