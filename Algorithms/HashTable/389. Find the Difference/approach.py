
# Counter
from collections import Counter

class Solution:
## use two couters
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter, t_counter = Counter(s), Counter(t)
        for tt in t:
            if tt not in s_counter or s_counter[tt] < t_counter[tt]:
                return tt
            
## or..
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter = Counter(s)
        t_counter = Counter(t)
        return [*(t_counter - s_counter)][0]
            
## use only one counter
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter = Counter(s)
        for tt in t:
            if tt not in s_counter or s_counter[tt] == 0:
                return tt
            else:
                s_counter[tt] -= 1

# XOR
    def findTheDifferenceXOR(self, s: str, t: str) -> str:
        char = 0
        for ss in s:
            char ^= ord(ss)
        for tt in t:
            char ^= ord(tt)
        return chr(char)
