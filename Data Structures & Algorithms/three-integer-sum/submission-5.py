class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triple = []
        for x in range(0, len(nums) - 1):
            for y in range(x + 1, len(nums)):
                sum = nums[x] + nums[y]
                for z in range(0, len(nums)):
                    if -1*sum == nums[z] and z != x and z != y:
                        hold = []
                        hold.append(nums[x])
                        hold.append(nums[y])
                        hold.append(-1*sum)
                        hold = sorted(hold)
                        if hold not in triple:
                            triple.append(hold)
        

        return triple

        