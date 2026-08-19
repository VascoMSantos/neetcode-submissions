class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        apperance = {}
        for num in nums:
            if num in apperance:
                return True
            else:
                apperance[num] = 1
        return False