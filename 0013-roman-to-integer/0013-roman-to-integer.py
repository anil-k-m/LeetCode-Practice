class Solution:
    def romanToInt(self, s: str) -> int:
        result_integer = 0
        index = len(s) - 1
        while index != -1:
            if s[index] == 'I':
                result_integer += 1
            elif s[index] == 'V':
                if index != 0 and s[index - 1] == 'I':
                    index -= 1
                    result_integer += 4
                else:
                    result_integer += 5
            elif s[index] == 'X':
                if index != 0 and s[index - 1] == 'I':
                    index -= 1
                    result_integer += 9
                else:
                    result_integer += 10
            elif s[index] == 'L':
                if index != 0 and s[index - 1] == 'X':
                    index -= 1
                    result_integer += 40
                else:
                    result_integer += 50
            elif s[index] == 'C':
                if index != 0 and s[index - 1] == 'X':
                    index -= 1
                    result_integer += 90
                else:
                    result_integer += 100
            elif s[index] == 'D':
                if index != 0 and s[index - 1] == 'C':
                    index -= 1
                    result_integer += 400
                else:
                    result_integer += 500
            elif s[index] == 'M':
                if index != 0 and s[index - 1] == 'C':
                    index -= 1
                    result_integer += 900
                else:
                    result_integer += 1000
            index -= 1
        return result_integer
