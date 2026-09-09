class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output = []
        # for i, num in enumerate(nums):
        #     nums_copy = nums.copy()
        #     nums_copy.pop(i)
        #     product = 1
        #     for num2 in nums_copy:
        #         product *= num2
        #     output.append(product)
        
        n = len(nums)
        output = [1] * n
        
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
            
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output