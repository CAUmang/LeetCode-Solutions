class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        k=0
        for i in range(2*len(nums)):
            ans.append(nums[k])
            k += 1
            if k == len(nums):
                k=0
        return ans