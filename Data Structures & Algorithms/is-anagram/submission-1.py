class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not (isinstance(s, str) and isinstance(t, str)):
            return False
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        