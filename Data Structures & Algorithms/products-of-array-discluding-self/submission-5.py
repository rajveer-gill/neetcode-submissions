class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for x in range(0, len(nums)):
            total = 1
            for i in range(0, len(nums)):
                if i != x:
                    total = total * nums[i]
            
            output.append(total)
        
        return output