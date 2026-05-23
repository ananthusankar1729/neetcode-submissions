class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x=""
        if len(word1)==len(word2):
            for i in range(len(word1)):
                x = x + word1[i]
                x = x + word2[i]
        elif len(word1) > len(word2):
            i=0
            while i < len(word2):
                x = x + word1[i]
                x = x + word2[i]
                i = i + 1
            while i < len(word1):
                x = x + word1[i]
                i = i+1
        elif len(word1) < len(word2):
            i=0
            while i < len(word1):
                x = x + word1[i]
                x = x + word2[i]
                i = i + 1
            while i < len(word2):
                x = x + word2[i]
                i = i+1
        return x 
        




        
            