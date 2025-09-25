class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word_1_len = len(word1)
        word_2_len = len(word2)
        larger_length = word_1_len if word_1_len > word_2_len else word_2_len
        new_word = ""
        for i in range(0, larger_length):
            word_1_char = word1[i] if i < word_1_len else ""
            word_2_char = word2[i] if i < word_2_len else ""
            new_word += word_1_char + word_2_char
        return new_word
