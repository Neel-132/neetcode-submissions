from collections import defaultdict
class Solution:
    def create_frequency_map(self, string, letters):
        freq_map = [0] * 26
        for letter in string:
            index = letters.index(letter)
            freq_map[index] += 1
        return tuple(freq_map)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_map = {}
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        if len(strs) == 1:
            return [strs]
        else:
            for string in strs:
                frequency_tuple = self.create_frequency_map(string, letters)
                if frequency_tuple not in char_map:
                    char_map[frequency_tuple] = [string]
                else:
                    char_map[frequency_tuple] += [string]
            return list(char_map.values())
