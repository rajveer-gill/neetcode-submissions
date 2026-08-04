class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for x in range(len(numbers)):
            looking = target - numbers[x]
            if looking in seen:
                return [seen[looking] + 1, x + 1]
            seen[numbers[x]] = x