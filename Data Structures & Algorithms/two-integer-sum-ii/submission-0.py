class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers is None or not numbers:
            return []
        
        i, j = 0, len(numbers)-1
        while i<j:
            add = numbers[i] + numbers[j]
            if add == target:
                return [i+1, j+1]
            elif add > target:
                j -= 1
            else:
                i += 1
        
        return []