class Solution:
    def is_start_of_sequence(self, hash_set, item):
        return (item - 1) not in hash_set

    def get_consecutive_seq_length(self, hash_set, item):
        count = 1
        for i in range(item + 1, item + len(hash_set)):
            if i in hash_set:
                count += 1
            else:
                break

        return count

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        hash_nums = set(nums)
        max_length = 1
        for item in nums:
            is_seq_start = self.is_start_of_sequence(hash_nums, item)
            if not is_seq_start:
                continue
            seq_length = self.get_consecutive_seq_length(hash_nums, item)
            if seq_length > max_length:
                max_length = seq_length

        return max_length