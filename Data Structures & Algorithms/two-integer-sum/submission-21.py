class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for x in range(0, len(nums)):
            if (target - nums[x]) in seen and x != seen[target - nums[x]]:
                if x < seen[target - nums[x]]:
                    return [x, seen[target - nums[x]]]
                else:
                    return [seen[target - nums[x]], x]
                
            seen[nums[x]] = x
