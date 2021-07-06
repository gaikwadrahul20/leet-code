def evalRPN( tokens):
        stack = []
        for token in tokens:
            if token in [ "+", "-", "*",  "/"]:
                a = stack.pop()
                b = stack.pop()
                if token == "+":
                    val = b + a
                elif token == "-":
                    val = b - a
                elif token == "*":
                    val = a * b
                elif token == "/":
                    val = int(b/ a)
                stack.append(val)
            else:
                stack.append(int(token))
        return stack.pop()

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
