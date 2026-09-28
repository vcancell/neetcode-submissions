class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for t in tokens:
            match t:
                case '+':
                    op2 = res.pop(-1)
                    op1 = res.pop(-1)
                    res.append(op1 + op2)
                case '-':
                    op2 = res.pop(-1)
                    op1 = res.pop(-1)
                    res.append(op1 - op2)
                case '*':
                    op2 = res.pop(-1)
                    op1 = res.pop(-1)
                    res.append(op1 * op2)
                case '/':
                    op2 = res.pop(-1)
                    op1 = res.pop(-1)
                    res.append(int(op1 / op2))
                case _:
                    res.append(int(t))
                
        return res[0]