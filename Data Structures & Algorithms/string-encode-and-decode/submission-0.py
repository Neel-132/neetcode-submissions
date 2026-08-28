class Solution:
    def create_ascii_map(self, strs:List[str]):
        strs_list = set("".join(strs).split())
        char_map = {}
        char_map_inv = {}
        for item in strs_list:
            char_map[item] = str(ord(item))
            char_map_inv[ord(item)] = item
        return char_map

    def create_ascii_inv(self, strs:List[str]):
        strs_list = set("".join(strs).split())
        char_map_inv = {}
        for item in strs_list:
            char_map_inv[ord(item)] = item
        return char_map_inv
    def encode(self, strs: List[str],delimiter = "*") -> str:
        encoded_str_final = ""
        if len(strs) == 0:
            return "#"
        for string in strs:
            encoded_str = ""
            if len(string) == 0:
                encoded_str = str(-1)
            else:
                for i in range(len(string)):
                    char = string[i]
                    if i!= len(string) - 1:
                        encoded_str += f"{ord(char)}{delimiter}"  
                    else:
                        encoded_str += f"{ord(char)}"
            encoded_str_final += f"{encoded_str} "
        return encoded_str_final.strip()      
        
    def decode(self, s: str, delimiter = "*") -> List[str]:
        string_list = s.split(" ")
        output = []
        print(string_list)
        if s == "#":
            return []
        for string in string_list:
            encoded_letters = string.split(delimiter)
            decoded_word = "".join([chr(int(letter)) if letter != "-1" else "" for letter in encoded_letters])
            output.append(decoded_word)
        return output


        

        
