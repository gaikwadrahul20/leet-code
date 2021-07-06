def decodeString(s):
        stack = []
        i = 0
        while i < len(s):
            if( s[i] == "]"):
                string = ""
                while True:
                    char = stack.pop()
                    if(char!= "["):
                        string = ''.join([char, string])
                    else:
                        break
                number = ''
                while(stack and stack[-1] in "0123456789"):
                    number = ''.join([stack.pop(), number])
                number = int(number)
                stack.append(number*string)
            else:
                stack.append(s[i])
            i+=1
            print(stack)
        ans = ""
        while(stack):
            ans = ''.join([stack.pop(), ans])
        return ans

print(decodeString("100[leetcode]"))
print(decodeString("3[a]2[bc]"))