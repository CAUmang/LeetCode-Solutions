class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if sum(nums)<0:
        #     return max(nums)
        # else:
        current_sum = 0
        max_now = float("-inf")
        pos = False
        for a in nums:
            if a >= 0:
                pos = True
            current_sum = max(current_sum+a, 0)
            max_now = max(current_sum, max_now)
        if pos:
            return max_now
        else:
            return max(nums)

        
        
        
        # k = 1
        # y=0
        # final_sum = float("-inf")
        # number_of_iterations = int( (len(nums)/2) * (1+len(nums)
        #                                             ) )
        # if len(nums) < 2:
        #     return nums[0]
        # else:
        #     for a in range(0, number_of_iterations):
        #         new_sum = sum(nums[y:y+k])
        #         print(nums[y:y+k])
        #         final_sum = max(final_sum, new_sum)
        #         y += 1
        #         if (y+k) > len(nums):
        #             k += 1
        #             y = 0
           
            # return final_sum
        
        
        # int( (len(nums)/2) * (1+len(nums)) )