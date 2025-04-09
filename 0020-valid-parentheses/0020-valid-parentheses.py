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