class Solution:
    def construct_delimiter_signature(self, s:str, delimiter):
        length = str(len(s))
        return length + delimiter

    def encode(self, strs: List[str], delimiter = "#") -> str:
        if len(strs) == 0:
            return "-1"

        encoded_string = ""
        for item in strs:
            del_sig = self.construct_delimiter_signature(item, delimiter)
            encoded_string += f"{del_sig}{item}"

        return encoded_string

    def decode(self, s: str, delimiter = "#") -> List[str]:
        decoded_string_list = []
        start = 0
        if s == "-1":
            return decoded_string_list

        if len(s) < 2:
            return decoded_string_list
        print("first:", s)
        while(start < len(s)):
            # delimiter = s[start]
            length_to_move = ""
            count = start
            while(s[count] != delimiter):
                length_to_move += s[count] 
                count += 1
            if int(length_to_move) == 0:
                decoded_string_list.append("")
                start += 2
            else:
                end_index = start + 1 + len(length_to_move) + int(length_to_move)
                decoded_string_list.append(s[start + len(length_to_move) + 1 : end_index])
                start = end_index
            
        return decoded_string_list



