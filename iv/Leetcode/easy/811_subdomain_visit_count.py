from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dom = {}
        for cp in cpdomains:
            count, domains_all = cp.split(" ")
            count = int(count)
            domains = domains_all.split(".")
            for i in range(len(domains)):
                domain = ".".join(domains[i:])
                if dom.get(domain):
                    dom[domain] += count
                else:
                    dom[domain] = count
        res = []
        for item in dom:
            ss = str(dom[item]) + " " + item
            res.append(ss)
        return res


    def subdomainVisits2(self, cpdomains: List[str]) -> List[str]:
        dom = {}
        for cp in cpdomains:
            for i in range(len(cp)):
                if cp[i] == " ":
                    start = i
                    count = int(cp[:i])
                if cp[i] == ".":
                    domain = cp[start+1:]
                    if dom.get(domain):
                        dom[domain] += count
                    else:
                        dom[domain] = count
                    start = i
            domain = cp[start + 1:]
            if dom.get(domain):
                dom[domain] += count
            else:
                dom[domain] = count

        # print(dom)
        res = []
        for item in dom:
            ss = str(dom[item]) + " " + item
            res.append(ss)
        return res


cpdomains = ["9001 discuss.leetcode.com"]
cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
s = Solution()
print(s.subdomainVisits(cpdomains))


