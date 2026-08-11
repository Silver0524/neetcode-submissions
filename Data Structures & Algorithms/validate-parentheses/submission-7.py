class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pmap = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for letter in s:
            if letter in pmap:
                if stack and stack[-1] == pmap[letter]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(letter)
        return True if not stack else False