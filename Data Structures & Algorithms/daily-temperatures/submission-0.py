class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            j = i+1
            count = 1
            while j< len(temperatures):
                if temperatures[i]<temperatures[j]:
                    break
                j+=1
                count+=1
            if j==len(temperatures):
                res.append(0)
            else:
                res.append(count)
        return res



            