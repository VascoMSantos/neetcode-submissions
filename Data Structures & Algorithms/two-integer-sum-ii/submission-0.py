class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(numbers)):
            difference = target - numbers[i]
            if difference in seen:
                return [seen[difference], i + 1]
            else:
                seen[numbers[i]] = i + 1
