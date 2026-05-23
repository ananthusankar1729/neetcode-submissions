class Solution:
    def calPoints(self, ops: List[str]) -> int:
        l=[]
        for op in ops:
            if op == "+":  
                l.append((l[-1]+l[-2]))
            elif op == "C":
                l.pop()
            elif op == "D":
                l.append((l[-1]*2))
            else:
                l.append(int(op)) 

        sum = 0
        for i in l:
            sum += i
        return sum





        