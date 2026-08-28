class Solution:
    def get_char_map(self):
        char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        char_map = {value:index for index, value in enumerate(char_list)}
        return char_map

    def get_frequency_map(self, s:str)->dict[str, int]:
        map = defaultdict(int)
        for letters in s:
            map[letters]+=1
        return map

    def collate_frequency_into_tuple(self, freq_map:dict[str, int], char_map):
        anagram_tup = [0] * 26
        for item in freq_map:
            anagram_tup[char_map[item]] = freq_map[item]
        return tuple(anagram_tup)
            
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_map = self.get_char_map()
        string_map = defaultdict(list)
        for string in strs:
            freq_map = self.get_frequency_map(string)
            anagram_tup = self.collate_frequency_into_tuple(freq_map, char_map)
            string_map[anagram_tup].append(string)
        return list(string_map.values())


            



        