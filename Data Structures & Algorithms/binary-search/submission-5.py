class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        hi = len(nums) - 1
        lo = 0

        if target not in nums:
            return -1

        while lo <= hi:
            middle = (hi + lo) // 2
            if nums[middle] == target:
                return middle
            else:
                if nums[middle] > target:
                    hi = middle - 1
                else:
                    lo = middle + 1