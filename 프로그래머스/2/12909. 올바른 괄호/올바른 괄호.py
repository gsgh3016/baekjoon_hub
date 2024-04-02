def solution(s):
    answer = True
    stack = []
    
    for c in s:
        if not stack and c == ')':
            return False
        elif c == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(c)
#        print(stack)
    
    if stack:
        return False
    return True