class Solution:
    def minOperations(self, logs: list) -> int:
        mystack = []
        for i in range(len(logs)):
            if logs[i] == "../":
                if len(mystack) > 0:
                    mystack.pop()
                continue
            elif logs[i] == "./":
                continue
            else:
                mystack.append(logs[i])
        return len(mystack)


logs = ["d1/","d2/","./","d3/","../","d31/"]
logs = ["d1/","../","../","../"]
logs = ["./", "../", "./"]
s = Solution()
print(s.minOperations(logs))

