from datetime import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        dd = datetime(year=year, day=day, month=month)
        print(dd.strftime('%A'))
        # print(dd.strptime('21-02-2020', '%d-%m-%Y'))


day = 31; month = 8; year = 2019
s = Solution()
print(s.dayOfTheWeek(day, month, year))
