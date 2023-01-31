from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        return True

assert Solution().containsDuplicate([1,2,3,1]) == True
