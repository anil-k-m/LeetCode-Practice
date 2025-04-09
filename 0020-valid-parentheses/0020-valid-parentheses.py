class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis_stack = []
        for p in s:
            if p in ['(', '[', '{']:
                paranthesis_stack.append(p)
            elif p == ')':
                if not paranthesis_stack or paranthesis_stack.pop() != '(':
                    return False
            elif p == ']':
                if not paranthesis_stack or paranthesis_stack.pop() != '[':
                    return False
            elif p == '}':
                if not paranthesis_stack or paranthesis_stack.pop() != '{':
                    return False
        if not paranthesis_stack:
            return True
        return False
        # paranthesis_count = {'(':0,'[':0,'{':0}
        # for paranthesis in s:
        #     if paranthesis == '(':
        #         paranthesis_count['('] += 1
        #     elif paranthesis == '[':
        #         paranthesis_count['['] += 1
        #     elif paranthesis == '{':
        #         paranthesis_count['{'] += 1
        #     elif paranthesis == ')':
        #         paranthesis_count['('] -= 1
        #     elif paranthesis == ']':
        #         paranthesis_count['['] -= 1
        #     elif paranthesis == '}':
        #         paranthesis_count['{'] -= 1
        #     if paranthesis_count['('] < 0 or paranthesis_count['['] < 0 or paranthesis_count['{'] < 0:
        #         return False
        # if paranthesis_count['('] == 0 and paranthesis_count['['] == 0 and paranthesis_count['{'] == 0:
        #     return True
        # return False
        