class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def left(s, amount):
            return s[:amount]
        
        short = float("inf")
        for n in strs:
            short = min(len(n), short)
        print(short)
        # print(len(strs))
        
        common = left(strs[0], short)
        print(left(common, short))
        k=0
        if short > 0:
            
            for n in range(500):
                if short == 0:
                    common = ""
                    return common
                else:
                    if left(common, short) == left(strs[k],short):
                        common = left(strs[k], short)
                        k += 1
                        if k >= len(strs):
                            return common
                            break
                    else:
                        short -= 1

        else:
            common = ""
            return common