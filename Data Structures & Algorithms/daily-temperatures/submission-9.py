class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        result = [0] * len(temp)
        stack = []

        for x in range(len(temp)):
            while stack and temp[x] > temp[stack[-1]]:
                prev = stack.pop()
                result[prev] = x - prev

            stack.append(x)
        
        return result

            