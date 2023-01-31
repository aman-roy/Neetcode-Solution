from typing import List 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1
        while l < r:
            res = max(res, min(height[l], height[r])*(r-l))
            if height[l] < height[r]:
                l += 1 
            else:
                r -= 1
        return res

assert (Solution().maxArea([1,8,6,2,5,4,8,3,7])) == 49
assert (Solution().maxArea([1,1])) == 1
