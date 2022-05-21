class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n==1:
            return strs[0]
        minimum_length = float('inf')
        for s in strs:
            minimum_length = min(minimum_length, len(s))
        if not minimum_length:
            return ""
        mini_str = min(strs, key=len)
        longest_prefix = 0
        flag = False
        for i in range(minimum_length):
            ith_letter =  mini_str[i]
            for j in range(n):
                curr = strs[j]
                if curr[i] != ith_letter:
                    return mini_str[:i]
            if i+1 == minimum_length:
                return mini_str
                
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     def left(s, amount):
#             return s[:amount]
        
#         short = float("inf")
#         for n in strs:
#             short = min(len(n), short)
#         print(short)
#         # print(len(strs))
        
#         common = left(strs[0], short)
#         print(left(common, short))
#         k=0
#         if short > 0:
            
#             for n in range(401):
#                 if short == 0:
#                     common = ""
#                     return common
#                 else:
#                     if left(common, short) == left(strs[k],short):
#                         common = left(strs[k], short)
#                         k += 1
#                         if k >= len(strs):
#                             return common
#                             break
#                     else:
#                         short -= 1

#         else:
#             common = ""
#             return common