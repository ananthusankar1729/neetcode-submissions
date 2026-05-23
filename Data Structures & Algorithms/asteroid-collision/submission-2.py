class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        l=[]
        for i in asteroids:
            while l and i<0 and l[-1]>0:
                diff = i + l[-1]
                if diff < 0:
                    l.pop()
                elif diff > 0:
                    i = 0
                else:
                    i = 0
                    l.pop()
            if i!=0:
                l.append(i)
        return l
            




