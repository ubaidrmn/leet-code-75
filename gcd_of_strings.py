class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str_1_is_smaller = True if len(str1) < len(str2) else False
        all_sub_strs = []
        smaller_string = str1 if str_1_is_smaller else str2
        larger_string = str2 if str_1_is_smaller else str1
        for i in range(len(smaller_string)):
            all_sub_strs.append(smaller_string[0:i+1])
        gcd = None
        for substr in all_sub_strs:
            if larger_string.replace(substr, "") == "" and smaller_string.replace(substr, "") == "":
                gcd = substr
        return gcd if gcd else ""
