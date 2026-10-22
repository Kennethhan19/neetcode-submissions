class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # time: O(N^2)
        # space: O(1)
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            # if a is 0, no numbers after can sum up to 0
            if a > 0:
                break
            
            # handle duplicate if it is same element as prev, just skip
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = a + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # handle duplicate if it is same element as prev, just skip
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res