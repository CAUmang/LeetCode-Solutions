class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2:
            return False
        mylist =[]
        d = {")":"(", "}":"{", "]":"["}
        for i in s:
            if i in d.values():
                mylist.append(i)
            elif len(mylist) and d[i] == mylist[-1]:
                mylist.pop()
            else:
                return False
        if len(mylist) == 0:
            return True
        
        