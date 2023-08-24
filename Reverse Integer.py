class Solution(object):
    def reverse(self, x):
        num = ""
        x = str(x)
        isMinus = False
        for i in range(len(x)-1,-1,-1):
            if x[i] != "-":
                num += x[i]
            else:
                isMinus = True

        if isMinus:
            num =  -int(num)
        else:
            num =  int(num)

        if num > (2 ** 31 - 1) or num < (-2 ** 31):
            return 0
        else:
            return num
