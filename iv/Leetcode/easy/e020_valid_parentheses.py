class Solution:
    def isValid(self, s: str) -> bool:
        mystack = [0]
        for i in range(len(s)):
            if s[i] in "({[":
                mystack.append(s[i])
            if s[i] == ")":
                if mystack[-1] != "(":
                    return False
                else:
                    mystack.pop(-1)
            if s[i] == "}":
                if mystack[-1] != "{":
                    return False
                else:
                    mystack.pop(-1)
            if s[i] == "]":
                if mystack[-1] != "[":
                    return False
                else:
                    mystack.pop(-1)

        if len(mystack) == 1:
            return True
        else:
            return False


if __name__ == "__main__":
    s = "()"
    s = "()[]{}"
    s = "(]"
    # s = "([)]"
    s = "{[]}"
    s = ")"
    sol = Solution()
    print(sol.isValid(s))
