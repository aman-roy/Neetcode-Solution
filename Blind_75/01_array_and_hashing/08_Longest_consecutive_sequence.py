from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_list = set(nums)

        longest = 0
        for n in nums:
            temp_long = 0
            if (n-1) not in new_list:
                while (n + temp_long) in new_list:
                    temp_long += 1
            longest = max(temp_long, longest)

        return longest


assert Solution().longestConsecutive([100,4,200,1,3,2]) == 4
assert Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
