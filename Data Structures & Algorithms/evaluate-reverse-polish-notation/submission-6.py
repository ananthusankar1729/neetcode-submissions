class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []                
        for i in tokens:                           
            if i == "+":
                res = int(s[-2]) + int(s[-1])
                s.pop()
                s.pop()
                s.append(res)
    
            elif i == "-":
                res = int(s[-2]) - int(s[-1])
                s.pop()
                s.pop()
                s.append(res)
            elif i== "*":
                res = int(s[-2])*int(s[-1])
                s.pop()
                s.pop()
                s.append(res)
            elif i == "/":
                res = int(float(s[-2]))/int((s[-1]))
                s.pop()
                s.pop()
                s.append(res)
            else:           
                s.append(i)
        return int(s[0])



