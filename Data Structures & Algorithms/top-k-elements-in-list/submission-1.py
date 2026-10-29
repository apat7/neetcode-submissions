class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for index, num in enumerate(nums):
            counts[num] = counts.get(num, 0) + 1

        return sorted(counts, key=counts.get, reverse=True)[:k]