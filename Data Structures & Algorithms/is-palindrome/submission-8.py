class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [c.lower() for c in s if c.isalnum()]

        for x in range(0, len(filtered) // 2):
            if filtered[x].lower() != filtered[len(filtered) - x - 1].lower():
                return False
        return True
        