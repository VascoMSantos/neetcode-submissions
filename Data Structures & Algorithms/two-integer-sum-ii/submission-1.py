class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(numbers)):
            difference = target - numbers[i]
            if difference in seen:
                return [seen[difference], i + 1]
            else:
                seen[numbers[i]] = i + 1

        # i = 0;
        # j = len(numbers) - 1;
       
        # while i < j:
        #     total = numbers[i] + numbers[j]
        #     if target > total:
        #        i += 1;
        #     elif target < total:
        #         j -=1;
        #     else:
        #         return [i+ 1 , j + 1]
