class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        num_set = set(nums)
        max_subseq = 1
        max_length = 1
        for item in num_set:
            current_seq_length = 1
            if (item - 1) not in num_set:
                while(True):
                    if (item + 1) in num_set:
                        current_seq_length += 1
                        item += 1
                    else:
                        break
            if max_length < current_seq_length:
                max_length = current_seq_length

        return max_length
                        


            
