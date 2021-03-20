class Solution:
    def isOneBitCharacter(self, bits: list) -> bool:
        if bits[-1] == 1:
            return False
        if len(bits) > 1 and bits[-2] == 0:
            return True
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                i += 2
            else:
                if i == (len(bits) - 1):
                    return True
                i += 1
        return False




bits = [1, 0, 0]
bits = [1, 1, 1, 0]
bits = [1]
bits = [0]
bits = [0,1,1,0]

s = Solution()
print(s.isOneBitCharacter(bits))

