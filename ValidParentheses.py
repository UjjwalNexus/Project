def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    
    return not stack

# Example usage
print(isValid("()"))     # Output: True
print(isValid("()[]{}")) # Output: True
print(isValid("(]"))     # Output: False
print(isValid("([)]"))   # Output: False
print(isValid("{[]}"))   # Output: True
