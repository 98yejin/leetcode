class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        string_chain_lengths = {word: 1 for word in words}
        for word in words:
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in string_chain_lengths:
                    string_chain_lengths[word] = max(string_chain_lengths[word], string_chain_lengths[prev]+1)
        return max(string_chain_lengths.values())