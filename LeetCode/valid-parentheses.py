class Solution:
    def isValid(self, s: str) -> bool:
        bracketStack = []
        
        for bracket in s:
            if bracket in '({[':
                bracketStack.append(bracket)
            else:
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