""""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
"""
class Solution():
    def canattendmeetings(self, intervals: list):
        # intervals = sorted(intervals, key=lambda x: x[0])
        intervals.sort(key=lambda x: x[0])

        start = -1
        end = -1
        intervals = sorted(intervals, key=lambda x: x[0])
        # intervals.sort(key=lambda x: x[0])

        start = -1
        end = -1
        for s1, e1 in intervals:
            # if start == -1:
            #     start = s1
            #     end = e1
            #     continue
            if s1 < end:
                return False
            end = e1
        return True


intervals = [[0,30],[5,10],[15,20]]
intervals = [[7,10],[2,4]]

s = Solution()
print(s.canattendmeetings(intervals))




