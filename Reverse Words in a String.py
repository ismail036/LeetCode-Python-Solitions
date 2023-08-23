class Solution(object):
    def reverseWords(self, s):
        s = s.split(" ")
        
        while "" in s:
              s.remove("")
                
        return (" ".join(list(reversed(s))))
