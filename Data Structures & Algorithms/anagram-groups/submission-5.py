class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        used = []
        final = []

        for x in range(0, len(strs)):
            hold = []
            if x in used:
                continue
            used.append(x)
            hold.append(strs[x])
            if x != len(strs) - 1:
                for y in range(x + 1, len(strs)):
                    if sorted(strs[x]) == sorted(strs[y]):
                        hold.append(strs[y])
                        used.append(y)

            final.append(hold)
        
        return final