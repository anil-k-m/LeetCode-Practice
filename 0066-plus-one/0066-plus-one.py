class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            ind = 0
            for i in range(len(digits)-1, -1, -1):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    ind = i+1
                    break
            if ind == 0:
                digits[ind] = 1
                digits.append(0)
            else:
                digits[ind] += 1
        else:
            digits[-1] += 1
        return digits