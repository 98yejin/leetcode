from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        common = Counter(nums).most_common(1)
        return common[0][0]