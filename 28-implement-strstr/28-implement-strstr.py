class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_n = len(needle)
        len_h = len(haystack)
        for a in range(len_h):
            if needle == haystack[a:a+len_n]:
                return a

        return -1   

        
        
        
        
        
        
        # def find(self, x, y):
        #     k = 0
        #     for a in y:
        #         if x == a
        #         return k
        #     else:
        #         k += 1