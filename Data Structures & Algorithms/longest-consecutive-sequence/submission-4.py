class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        streak = 0

        for num in nums_set:
            if num-1 not in nums_set:
                current = num
                cur_streak = 1

                while current+1 in nums_set:
                    cur_streak += 1
                    current += 1
                streak = max(cur_streak, streak)

        return streak