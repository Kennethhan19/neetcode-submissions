class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two loop
        # O(N^2)
        # O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return[i, j]

        # sort then 2 pointer
        # O(NlogN)
        # O(N)
        # sorted_num = []

        # for i in range(len(nums)):
        #     sorted_num.append([nums[i], i])

        # sorted_num.sort()
 
        # i, j = 0, len(sorted_num)-1
        # while i < j:
        #     add_res = sorted_num[i][0] + sorted_num[j][0]
        #     if add_res == target:
        #         x = sorted_num[i][1]
        #         y = sorted_num[j][1]
        #         return [min(x,y), max(x,y)]
        #     elif add_res > target:
        #         j -= 1
        #     else:
        #         i += 1
        
        # Hashmap to track items and its index
        # for every number, check if target - num is in map
        # if yes, we have a pair
        # time: O(N)
        # space: O(N)
        numsMap = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in numsMap:
                return [numsMap[x], i]
            numsMap[nums[i]] = i

        
           