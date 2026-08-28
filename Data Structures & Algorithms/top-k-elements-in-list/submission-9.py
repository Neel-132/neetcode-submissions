class Solution:
    def frequencymap(self, nums):
        map = defaultdict(int)
        for item in nums:
            map[item] += 1
        return map
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)
        topkfrequencies = [0] * (l + 1)
        freqmap = self.frequencymap(nums)
        for item in freqmap:
            frequency = freqmap[item]
            if isinstance(topkfrequencies[l - frequency], list) and len(topkfrequencies[l - frequency]) > 0:
                topkfrequencies[l - frequency] += [item]
            else:
                topkfrequencies[l - frequency] = [item]

        result = []
        
       
        for i in range(0, l + 1):
            if k == 0:
                break
            if topkfrequencies[i] == 0:
                continue
            result.extend(topkfrequencies[i])
            k -= len(topkfrequencies[i])

        return result


        