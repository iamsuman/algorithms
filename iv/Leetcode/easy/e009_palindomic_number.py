class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        if x < 0:
            return False
        if x < 10:
            return True
        rev = 0
        while x > 0:
            rev = rev * 10 + (x % 10)
            x = x // 10
        # print(rev)
        if rev == num:
            return True
        else:
            return False

    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        x_list = list(str(x))
        i, j = 0, len(x_list) - 1
        while i < j:
            if x_list[i] != x_list[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    x = 121
    x = -121
    x = 10
    x = -101
    s = Solution()
    print(s.isPalindrome(x))
