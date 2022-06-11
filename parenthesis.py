def parenthesis(s):
    stack = []
  
    for i in range(len(s)):
        if s[i] in ["(", "{", "["]:
  
            stack.append(s[i])
        
        elif s[i] in [")", "}", "]"]:
            if not stack:
                return False
            stack_char = stack.pop()
            if stack_char == '(':
                if s[i] != ")":
                    return False
            if stack_char == "{":
                if s[i] != "}":
                    return False
            if stack_char == "[":
                if s[i] != "]":
                    return False
    if len(stack) != 0:
        print("Not balanced")
    else:
        return True

s = "a(b)"       
parenthesis(s)