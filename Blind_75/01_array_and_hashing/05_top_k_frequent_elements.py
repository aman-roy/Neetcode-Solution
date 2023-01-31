from typing import List

# O(NlogN)
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         print([[] for _ in range(len(nums) + 1)])
#         freq = {}
#         for num in nums:
#             if num in freq:
#                 freq[num] += 1
#             else:
#                 freq[num] = 1
#
#         freq = dict(sorted(freq.items(), key=lambda item: item[1]))
#
#         result = list()
#         for _ in range(k):
#             result.append(freq.popitem()[0])
#
#         return result
#
# assert Solution().topKFrequent([1,1,1,2,2,3], 2) == [1,2]
# assert Solution().topKFrequent([1], 1) == [1]

waht = 7
# O(n) The fassst solution apparantely 
class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums)+1)]
        for n, f in freq.items():
            bucket[f].append(n)
        
        ans = list()
        for i, _ in enumerate(bucket):
            for item in bucket[len(nums)-i]:
                if len(ans) == k:
                    break
                ans.append(item)
        return ans


assert Solution1().topKFrequent([1,1,1,2,2,3], 2) == [1,2]
assert Solution1().topKFrequent([1], 1) == [1]

