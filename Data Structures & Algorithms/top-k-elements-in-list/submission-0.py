class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sort = {}
        count = []

        for i in range(len(nums)):
            if nums[i] in sort:
                sort[nums[i]] += 1
            else:
                sort[nums[i]] = 1
        
        sort = dict(sorted(sort.items(), key=lambda item: item[1], reverse=True))
        
        for key, value in sort.items():
            if len(count) < k:
                count.append(key)

        return count