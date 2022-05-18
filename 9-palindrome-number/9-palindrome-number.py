class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = []
        rev = []
        a = -1
        y = ""
        if x<0:
            return False
        
        while x>=10:
            nums.append(x%10)
            x = x//10
        nums.append(x)
        rev = nums[::-1]
        
        for i in range(len(nums)):
            if nums[i] != rev[i]:
                return False
        return True
        
        # print(nums)
        # print(nums[::-1])
#         nums = [str(i) for i in str(x)]
                    
#         for k in range(len(nums)):
#             rev.append(nums[a])
#             a -= 1
#         for j in rev:
#             y += str(j)



#         if str(x) ==str(y):
#             return True
#         else:
#             False

        