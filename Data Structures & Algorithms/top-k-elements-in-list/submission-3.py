from collections import defaultdict
class Solution:
    def create_count_map(self, nums: List[int]):
        freq_map = defaultdict(int)
        for item in nums:
            freq_map[item] += 1
        return freq_map

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums) 
        frequency_list = [0] * (n + 1)  
        final_list = []
        freq_map = self.create_count_map(nums)
        for item in nums:
            val = frequency_list[freq_map[item]]
            if val == 0:
                frequency_list[freq_map[item]] = [item]
            else:
                if item not in val:
                    frequency_list[freq_map[item]] += [item]
       
        for i in range(len(frequency_list)-1, -1, -1):
            item = frequency_list[i]
            if k == 0:
                return final_list
            if item == 0:
                continue
            if isinstance(item, list):
                if k < len(item):
                    final_list.extend(item[:k])
                    k = 0
                else:
                    final_list.extend(item)
                    k -= len(item)
                

            


        