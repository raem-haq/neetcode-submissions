def is_num(x):
    try:
        int(x)
    except ValueError:
        return False
    return True

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stck = []
        for t in tokens:
            if is_num(t): # only works for pos integers
                stck.append(int(t))
            else:
                a = stck.pop()
                b = stck.pop()
                if t == '+': 
                    stck.append(a+b)
                elif t == '-':
                    stck.append(b-a)
                elif t == '/':
                    stck.append(int(b/a)) # trunc towards 0
                elif t == '*':
                    stck.append(a*b)
        return stck.pop()