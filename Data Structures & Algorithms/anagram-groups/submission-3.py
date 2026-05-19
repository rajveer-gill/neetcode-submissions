class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        megaList = []
        stringChecker = set()

        if len(strs) == 1:
            megaList.append([strs[0]])
            return megaList

        for x in range(0, len(strs)):
            anaGroup = []
            if x in stringChecker:
                continue
            else:
                anaGroup.append(strs[x])
                stringChecker.add(x)
                i = x + 1
                while i < len(strs):
                    if i not in stringChecker and sorted(strs[i]) == sorted(strs[x]):
                        stringChecker.add(i)
                        anaGroup.append(strs[i])
                    i = i + 1
                megaList.append(anaGroup)
        

        return megaList

