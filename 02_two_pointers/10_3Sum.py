from typing import List

# Not so efficient solution, I guess!
class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_res = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if (nums[i]+nums[j]+nums[k]) == 0: 
                        x, y, z = sorted([nums[i], nums[j], nums[k]])
                        final_res.add((x,y,z))
        
        final_res_list = []  
        for item in final_res:
            final_res_list.append([*item])
        return final_res_list

print(Solution1().threeSum([-1,0,1,2,-1,-4]))
print(Solution1().threeSum([0,1,1]))
print(Solution1().threeSum([0,0,0]))


# Faster Solution 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_res = []
        nums.sort()

        for i, val in enumerate(nums):
            # Don't entertain the positive numbers
            if val > 0:
                break

            # Skip the repititive numbers 
            if i > 0 and val == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if temp == 0:
                    final_res.append([nums[i],nums[l],nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif temp > 0:
                    r -= 1
                else:
                    l += 1

        return final_res

print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([0,1,1]))
print(Solution().threeSum([0,0,0]))
