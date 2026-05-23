class Solution:
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        chars, chart = {},{}
        for i in s:
            chars[i] = 1 + chars.get(i, 0)
        for i in t:
            chart[i] = 1 + chart.get(i,0)
        
        for i in chars:
            if chars.get(i,0)!=chart.get(i, 0):
                return False
        return True
        