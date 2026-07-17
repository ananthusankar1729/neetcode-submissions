class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        word = ""
        for i in s:
            if i.isalnum():
                word = word + i
        if len(word)<=1:
            return True
        l, r = 0, len(word)-1
        while l<=r:
            if word[l]!=word[r]:
                return False
            l+=1
            r-=1
        return True
