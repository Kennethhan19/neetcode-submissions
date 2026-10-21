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
       
        # freq = {}
        # for n in nums:
        #     if n in freq:
        #         freq[n] += 1
        #     else:
        #         freq[n] = 1

        # arr = []
        # for num, cnt in freq.items():
        #     arr.append([cnt, num])
        # arr.sort()

        # res = []
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        # return res

        # sol 2
        # count using hashmap
        # use min heap to track k elements
        # heap push/pop is logK 
        # time: O(nlogk)
        # space: O(n)

        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        arr = []
        for n, c in freq.items():
            heapq.heappush(arr, [c, n])
            if len(arr) > k:
                heapq.heappop(arr)

        res = []
        while arr:
            res.append(heapq.heappop(arr)[1])
        return res