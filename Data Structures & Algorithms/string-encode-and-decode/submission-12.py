from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        previous = None
        result = ""
        if len(strs) == 0:
            return ""
        for i in range(len(strs)):
            curr_length = len(strs[i])
            result += f"{curr_length}#{strs[i]}"
        return result



    def decode(self, s: str) -> List[str]:
        decoded_str = []
        number = ""
        decoded_curr = ""
        if len(s) == 0:
            return []
        to_ignore = False
        for i in range(len(s)):
            if s[i].isdigit() and not to_ignore: 
                number += s[i]
            elif s[i] == "#" and not to_ignore:
                number = int(number)
                if number == 0:
                    decoded_str.append("")
                    to_ignore = False
                    number = ""
                else:
                    to_ignore = True
                
            else:
                if number > 0:
                    decoded_curr += s[i]
                    number -= 1
                    if number == 0:
                        decoded_str.append(decoded_curr)
                        to_ignore = False
                        number = ""
                        decoded_curr = ""
                
        return decoded_str

