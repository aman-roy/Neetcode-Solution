class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        max_freq = ""
        max_len = -1
        for right in range(len(s)):
            if s[right] in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1

            if max_freq == "" or freq[s[right]] > freq[max_freq]:
                max_freq = s[right]

            if (right - left + 1) - freq[max_freq] > k:
                freq[s[left]] -= 1
                left += 1

            max_len = max(max_len, right-left+1)

        return max_len



print(Solution().characterReplacement("ABAB", 2))
print(Solution().characterReplacement("AABABBA", 1))
