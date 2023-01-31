from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = dict()
        final = list()
        for (i, n) in enumerate(nums):
            if n in res:
                final = [i, res[n]]
                break
            res[target-n] = i
        return final

assert Solution().twoSum([2,7,11,15], 9) == [2,0]
