class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
                
        mylist = []
        for i in range(len(nums)):
            if i<len(nums) and nums[i] in nums[0:i]:
                mylist.append(i)
        # print(mylist)
        for n in range(len(mylist)):
            # if n <2:
            #     nums += [nums.pop(mylist[0])]
            #     print(nums)
            # else:
            nums += [nums.pop(mylist[n]-n)]
            # print(nums)
        return len(nums)-len(mylist)
        