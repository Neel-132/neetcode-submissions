class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while(left < right):
            summand = numbers[left] + numbers[right]
            if summand == target:
                if left > right:
                    return [right + 1, left + 1]
                return [left + 1, right + 1]
            elif summand > target:
                right -= 1
            else:
                left += 1





        