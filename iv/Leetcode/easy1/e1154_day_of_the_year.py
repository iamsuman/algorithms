class Solution:
    def dayOfYear(self, date: str) -> int:
        days = [31,28,31,30,31,30,31,31,30,31,30,31]

        dt = date.split("-")
        yr = int(dt[0])
        mm = int(dt[1])
        dd = int(dt[2])

        if yr % 4 == 0 and not (yr % 100 == 0 and yr % 400 != 0):
            days[1] = 29

        no_day = sum(days[:(mm - 1)]) + dd
        return no_day


date = "2019-01-09"
date = "2019-02-10"
date = "1900-03-01"
# date = "2000-03-01"
s = Solution()
print(s.dayOfYear(date))
