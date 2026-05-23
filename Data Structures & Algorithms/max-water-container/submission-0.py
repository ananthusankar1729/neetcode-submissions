class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=[]
        for i in range(len(heights)-1):
            for j in range(i+1,len(heights)):
                amt = (j-i)*min(heights[i],heights[j])
                l.append(amt)
        return max(l)
        
        