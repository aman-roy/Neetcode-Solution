from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for s in strs:
            sw = ''.join(sorted(s))
            if sw in dictionary:
                dictionary[sw] += [s]
            else:
                dictionary[sw] = [s]
        return [e for e in dictionary.values()] 


print(Solution().groupAnagrams(['bat', 'nat', 'ate', 'tan', 'tea', 'eat'])) 
assert Solution().groupAnagrams(['bat', 'nat', 'ate', 'tan', 'tea', 'eat']) == [["bat"],["nat","tan"],["ate","tea","eat"]]
assert Solution().groupAnagrams([""]) == [[""]]
assert Solution().groupAnagrams(["a"]) == [["a"]]
