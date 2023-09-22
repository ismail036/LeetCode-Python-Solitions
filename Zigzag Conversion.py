class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = [[] for row in range(numRows)]

        if len(s) <= numRows or numRows == 1:
            return s
        
        row = 0
        step = 1
        for i in s:
            rows[row].append(i)
            if row == numRows-1:
                step = -1
            elif row == 0 :
                step = 1
            row += step
        conversion = ""

        for i in rows:
            conversion += "".join(i)
        
        return conversion
        
    



            
        
