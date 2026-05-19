class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}

        for i, num in enumerate(nums):
            find = target - num
            if find in found:
                return [found[find], i]
            
            found[num] = i