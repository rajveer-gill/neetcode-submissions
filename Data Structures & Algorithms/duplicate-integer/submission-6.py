class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = False
        iterate = 0

        while iterate <= (len(nums) - 2) and found == False:
            if nums[iterate] in nums[(iterate + 1):]:
                found = True
            else:
                iterate = iterate + 1
        
        return found