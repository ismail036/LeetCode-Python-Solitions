class Solution(object):
    def longestPalindrome(self, s):
        for i in range(len(s)):
            p = 0
            for k in range(0,i+1):
                k = (s[k:len(s)-i+1+p])
                p = p+1
                if k == k[::-1]:
                    return k

    
