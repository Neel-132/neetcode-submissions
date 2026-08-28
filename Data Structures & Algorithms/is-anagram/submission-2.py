class Solution:
    def create_frequency_hash(self, s:str):
        hashmap = {}
        for letter in s:
            count = 1
            if letter in hashmap:
                count = hashmap[letter]
                count += 1
                hashmap[letter] = count
            else:
                hashmap[letter] = count
        return hashmap



    def isAnagram(self, s: str, t: str) -> bool:
        if not (isinstance(s, str) and isinstance(t, str)):
            return False
        if len(s) != len(t):
            return False
        hash_s = self.create_frequency_hash(s)
        hash_t = self.create_frequency_hash(t)
        if hash_s == hash_t:
            return True
        return False        