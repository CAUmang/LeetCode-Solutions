class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = []
        rev = []
        a = -1
        y = ""
        nums = [str(i) for i in str(x)]
        for k in range(len(nums)):
            rev.append(nums[a])
            a -= 1
        for j in rev:
            y += str(j)
        
        if str(x) ==str(y):
            return True
        else:
            False