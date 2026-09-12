class Solution:
    def alphanumeric_char(self, character :str):
        return character.isalnum()

        
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        left = 0
        right = len(s) - 1
    
        while (left < right):
            if not self.alphanumeric_char(s[left]) or not self.alphanumeric_char(s[right]):
                if not self.alphanumeric_char(s[left]):
                    left += 1
                if not self.alphanumeric_char(s[right]):
                    right -= 1
                continue
            else:
                if s[left].lower() != s[right].lower():
                    return False

                else:
                    left += 1
                    right -= 1

        return True
            