class Atoi():
    def myatoi(self, s: str) -> int:
        start = True
        ret = ""
        for i in list(s):
            if i == " ":
                if not start:
                    break
            elif i == "+" or i == "-":
                if start:
                    start = False
                    ret = ret + i
                else:
                    break
            elif i.isdigit():
                start = False
                ret = ret + i
            else:
                break
        try:
            ret = int(ret)
        except:
            ret = "0"
        if -2**31 >= int(ret):
            ret = -2147483648
        elif int(ret) > 2**31 - 1:
            ret = 2**31 - 1
        return int(ret)


s = "42"
s = "   -42-"
# s = "4193 with words"
# s = "words and 987"
# s = "-91283472332"
# s = "3.14159"
# s = " "
# s = "+-2"
a = Atoi()
print(a.myatoi(s))
