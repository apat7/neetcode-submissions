class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_len = 0
        sliding = set()

        while right < len(s):
            if s[right] not in sliding:
                sliding.add(s[right])
                right += 1
            else:
                sliding.remove(s[left])
                left += 1
            max_len = max(max_len, len(sliding))

        return max_len