class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(0, len(nums) - 1):
            first = nums[x]
            find = target - first
            for y in range(x + 1, len(nums)):
                if nums[y] == find:
                    return [x, y]
