class Solution:
    def construct_delimiter_signature(self, s:str, delimiter):
        length = str(len(s))
        return delimiter + length + delimiter

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
        print(s)
        while(start < len(s)):
            delimiter = s[start]
            length_to_move = ""
            for i in range(start + 1, len(s)):
                if s[i] != delimiter:
                    length_to_move += s[i]  
                else:
                    break
            encoding_index = len(length_to_move) 
            
            length_to_move = int(length_to_move)
            if length_to_move == 0:
                decoded_string_list.append("")
                start += 3
            else:
                decoded_string_list.append(s[start + encoding_index + 2 : start + encoding_index + 2 + length_to_move])
                start = start + encoding_index + 2 + length_to_move
            
        return decoded_string_list



