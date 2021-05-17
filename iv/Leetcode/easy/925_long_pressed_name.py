class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name1 = []
        typed1 = []
        s = ""
        for i in range(len(name)):
            if i == 0 or name[i] == name[i-1]:
                s += name[i]
            else:
                name1.append(s)
                s = name[i]
        if len(s) != 0:
            name1.append(s)

        s = ""
        for i in range(len(typed)):
            if i == 0 or typed[i] == typed[i-1]:
                s += typed[i]
            else:
                typed1.append(s)
                s = typed[i]
        if len(s) != 0:
            typed1.append(s)

        if len(name1) != len(typed1):
            return False
        else:
            for i in range(len(name1)):
                if name1[i] not in typed1[i]:
                    return False
            return True


name = "alex"; typed = "aaleex"
name = "saeed"; typed = "ssaaedd"
name = "leelee"; typed = "lleeelee"
name = "t";  typed = "x"
sol = Solution()
print(sol.isLongPressedName(name, typed))



