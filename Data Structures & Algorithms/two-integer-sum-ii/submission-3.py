class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        l=[]
        for i in range(0,len(numbers)-1):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    l.append(i+1)
                    l.append(j+1)
        return l
