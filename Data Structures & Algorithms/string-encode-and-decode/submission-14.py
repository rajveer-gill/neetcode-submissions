class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""

        for x in strs:
            final = final + str(len(x)) + '#' + x

        return final

    def decode(self, s: str) -> List[str]:
        count = 0
        final = []

        while count < len(s):
            j = count
            
            while j < len(s) and s[j].isdigit():
                j = j + 1
            
            if s[j] == '#':
                wordLen = int(s[count: j])
                word = s[j + 1: j +1 + wordLen]

                final.append(word)
                count = j + 1 + wordLen
            
        
        return final
