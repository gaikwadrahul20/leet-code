def isValid(s):
    stack = []
    opened = {
        "(": ")",
        "{": "}",
        "[":"]"
    }
    for char in s:
        if char in opened.keys():
            stack.append(char)
        elif(not stack):
            return False
        elif opened[stack.pop()] != char:
            return False
        print(stack)
    if (not stack):
        return True
    else:
        return False

print(isValid("{"))