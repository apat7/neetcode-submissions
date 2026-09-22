class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left = i
            right = len(numbers)-1
            while (left<right):
                sum = numbers[left] + numbers[right]
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    return [left+1, right+1]


        