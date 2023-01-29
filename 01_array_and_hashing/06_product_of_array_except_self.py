from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        zerocount = 0
        for i in nums:
            if zerocount > 1:
                break
            if i == 0:
                zerocount += 1
                continue
            mult *= i
        if zerocount > 1:
            return [0 for _ in range(len(nums))]
        elif zerocount == 0:
            return [mult//x for x in nums]
        else:
            return [0 if x != 0 else mult for x in nums]

assert Solution().productExceptSelf([1,2,3,4]) == [24,12,8,6]
assert Solution().productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]


class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in range(len(nums))]

        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        print(res)
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        print(res)
        return res


assert Solution1().productExceptSelf([1,2,3,4]) == [24,12,8,6]
assert Solution1().productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]

