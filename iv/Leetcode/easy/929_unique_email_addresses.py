"""
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'
find the unique email addresses
"""
from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        def validemail(email: str):
            local_name = email.split("@")[0]
            domain_name = email.split("@")[1]
            res = ""
            if local_name:
                for c in local_name:
                    if c.isalpha():
                        res += c
                    if c == "+":
                        break
                return res + "@" + domain_name
            else:
                return None

        ans = set()
        for email in emails:
            ans.add(validemail(email))
        # print(ans)

        return len(ans)


emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
s = Solution()
print(s.numUniqueEmails(emails))


