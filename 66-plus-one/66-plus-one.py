class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if min(digits) == 9:
            digits[0] = 1
            for n in range(1, len(digits)):
                digits[n] = 0
            digits.append(0)
        elif digits[-1] == 9:
            for n in range(len(digits)-1, -1, -1):
                if digits[n] != 9:
                    digits[n] = digits[n]+1
                    break
                else:
                    digits[n] = 0
        else:
            digits[-1] += 1
        return digits