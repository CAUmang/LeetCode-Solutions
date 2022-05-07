class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i = 0
        # k = 1
        # length = len(nums)
        # number = length*(length+1)
        # for n in range(100000000):
        #     if i != k:
        #         sum = nums[i] + nums[k]
        #         if sum == target:
        #             return([i,k])
        #             break
        #         else:
        #             k += 1
        #             if k == length:
        #                 k = 1
        #                 i += 1
        #                 sum = 0
        #             else:
        #                 sum = 0
        #     else:
        #         k += 1
        #         sum=0

        d ={}
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]], i]
            d[target-nums[i]] = i
                