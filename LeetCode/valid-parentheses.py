'''
- Use a stack (can be implemented using the list from python)
'''
class Solution:
    def isValid(self, s: str) -> bool:
        bracketStack = []
        
        for bracket in s:
            if bracket in '({[':
                bracketStack.append(bracket)
            else:
                # -1 looks at top element (aka the end of the list)
                peekElement = bracketStack[-1] if bracketStack else None
                if (
                    (bracket == ')' and peekElement == '(') or \
                    (bracket == '}' and peekElement == '{') or \
                    (bracket == ']' and peekElement == '[')
                ):
                    bracketStack.pop()
                else:
                    return False # there should be a matching element

        return not bracketStack  