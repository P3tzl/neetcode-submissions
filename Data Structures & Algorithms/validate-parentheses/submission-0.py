class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        stack = []
        for a in s:
            if a in valid_dict.keys():
                if len(stack)==0:
                    return False
                elif stack[-1] == valid_dict[a]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(a)
        if len(stack)==0:
            return True
        return False