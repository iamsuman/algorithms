class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        if a == b:
            seen = set()
            for ss in a:
                if ss in seen:
                    return True
                seen.add(ss)
            return False
        else:
            start = -1
            end = -1
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
                    if count > 2:
                        return False
                    if start == -1:
                        start = i
                    else:
                        end = i
            if count != 2:
                return False
            if a[start] == b[end] and a[end] == b[start]:
                return True

a = "ab"; b = "ba"
# a = "ab"; b = "ab"
# a = "aa"; b = "aa"

s = Solution()
print(s.buddyStrings(a, b))

