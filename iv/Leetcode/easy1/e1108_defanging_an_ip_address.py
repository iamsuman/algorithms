class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = []
        for st in address.split("."):
            res.append(st)
        return "[.]".join(res)


address = "1.1.1.1"
s = Solution()
print(s.defangIPaddr(address))
