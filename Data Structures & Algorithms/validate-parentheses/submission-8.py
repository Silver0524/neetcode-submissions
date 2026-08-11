class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pmap = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for letter in s:
            if letter in pmap.values():
                stack.append(letter)
            elif letter in pmap:
                if not stack:
                    return False
                elif stack[-1] == pmap[letter]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False