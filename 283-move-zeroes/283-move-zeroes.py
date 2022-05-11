class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # j = 0
        # number = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[j] = nums[i]
        #         j += 1
        #     else:
        #         number += 1
        # k = -1
        # for n in range(number):
        #     nums[k] = 0
        #     k -= 1
        
        j = 0
        for i in range(len(nums)):
            if nums[j] == 0:
                nums += [nums.pop(j)]
            else:
                j += 1
                
            
        