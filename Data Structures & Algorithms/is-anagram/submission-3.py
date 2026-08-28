class Solution:
    def getfrequencymap(self, s:str) -> dict[str, int]:
        map = defaultdict(int)
        for letter in s:
            map[letter] += 1
        return map
        
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = self.getfrequencymap(s)
        t_map = self.getfrequencymap(t)
        return s_map == t_map

        