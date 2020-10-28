"""
Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_hash = {}
        for ss in s:
            if char_hash.get(ss):
                char_hash[ss] += 1
            else:
                char_hash[ss] = 1

        maxodd = 0
        res = 0
        odd = False
        for chars in char_hash:
            if char_hash[chars] % 2 == 0:
                res += char_hash[chars]
            else:
                odd = True
                res = res + char_hash[chars] - 1
        if odd:
            res = res + 1
        return res


    def longestPalindrome2(self, s: str) -> int:
        char_hash = {}
        for ss in s:
            if char_hash.get(ss):
                char_hash[ss] += 1
            else:
                char_hash[ss] = 1

        maxodd = 0
        res = 0
        for chars in char_hash:
            if char_hash[chars] % 2 == 0:
                res += char_hash[chars]
            else:
                if char_hash[chars] > maxodd:
                    if maxodd > 0:
                        res = res + maxodd - 1
                    maxodd = char_hash[chars]
                else:
                    res = res + char_hash[chars] - 1
        res = res + maxodd

        return res


s = "abccccdd"
s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"

sol = Solution()
print(sol.longestPalindrome(s))





