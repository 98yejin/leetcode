class Solution:
    # use two-pointers
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        n, m = len(s), len(t)
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n

    # use for-loop
    def isSubsequence(self, s: str, t: str) -> bool:
        i, n = 0, len(s)
        for char in t:
            if i < n and s[i] == char:
                i += 1
        return i == n