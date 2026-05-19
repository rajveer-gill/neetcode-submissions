class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final = []

        for x in range(0, len(nums) - 1):
            for i in range((x + 1), len(nums)):
                print(nums[x])
                print(nums[i])
                if (nums[x] + nums[i]) == target:
                    final.append(x)
                    final.append(i)
                    return final

        
        





        