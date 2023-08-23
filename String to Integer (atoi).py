class Solution(object):
    def myAtoi(self, s):
        number = ""
        numbers = "1234567890"
        for i  in s:
            if i == " " and number == "":
               continue
            elif i == "-" and number == "":
                number += i
            elif i == "+" and number == "":
                number += " "
            elif i in numbers:
                number += i
            else:
                if number != "":
                    try:
                       number = int(number)
                    except:
                        return 0
                    if number < -2147483648:
                        return -2147483648
                    elif number > 2147483647:
                         return 2147483647
                    else:
                        return number
                else:
                     return 0
        if number != "":    
            number = int(number)
            if number < -2147483648:
                return -2147483648
            elif number > 2147483647:
                return 2147483647
            else:
                return number
        else:
            return 0
        
        return 0
