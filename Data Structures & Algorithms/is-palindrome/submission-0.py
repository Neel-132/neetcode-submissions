class Solution:
    def check_is_alphanumeric(self, char:str):
        if (ord(char) >= 48 and ord(char) <= 57) or (ord(char.upper()) >= 65 and ord(char.upper()) <= 90):
            return True

        return False

    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join([char.lower() for char in s if self.check_is_alphanumeric(char)])
        print([char for char in s if self.check_is_alphanumeric(char)])
        if len(cleaned_s) <= 1:
            return True
        i = 0
        j = len(cleaned_s) - 1
        while(i < j):
            if cleaned_s[i] != cleaned_s[j]:
                return False
            i += 1
            j -= 1
        return True
        