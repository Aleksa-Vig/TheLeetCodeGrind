class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        parenthesisMap = {')':'(', '}':'{', ']':'['}

        # Time complexity: O(n)
        # Space complexity: O(n)

        for c in s:

            ##appears as key
            if c not in parenthesisMap: 
                stack.append(c)
                continue
            
            if c in parenthesisMap:
                if not stack or parenthesisMap[c] != stack[-1]:
                    return False
                
                stack.pop()

        return not stack