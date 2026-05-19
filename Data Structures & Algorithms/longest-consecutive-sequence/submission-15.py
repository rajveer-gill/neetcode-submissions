class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        print(nums)
        numHold = nums[0]
        tempStreak = 1
        topStreak = 0
        
        for x in range(1,len(nums)):
            if nums[x] == nums[x - 1]:
                continue
            elif nums[x] == nums[x - 1] + 1:
                tempStreak = tempStreak + 1
            else:
                if tempStreak >= topStreak:
                    topStreak = tempStreak
                    tempStreak = 1
        
        if tempStreak >= topStreak:
                    topStreak = tempStreak
                    tempStreak = 1
        
        return topStreak



        